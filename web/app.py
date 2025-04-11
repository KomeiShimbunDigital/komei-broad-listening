from flask import Flask, render_template,render_template_string, request, redirect, url_for, send_from_directory, flash
import os
import subprocess
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # フラッシュメッセージ用

# パス設定
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
INPUT_DIR = os.path.join(BASE_DIR, 'scatter/pipeline/inputs')
CONFIG_DIR = os.path.join(BASE_DIR, 'scatter/pipeline/configs')
OUTPUT_DIR = os.path.join(BASE_DIR, 'scatter/pipeline/outputs')
OUTPUT_BASE_DIR = os.path.join(os.getcwd(), 'scatter/pipeline/outputs')
MAIN_SCRIPT = os.path.join(BASE_DIR, 'scatter/pipeline/main.py')


@app.route('/')
def index():
    projects = []
    for file in os.listdir(CONFIG_DIR):
        if file.endswith('.json'):
            name = file[:-5]
            output_path = os.path.join(OUTPUT_DIR, name, 'report', 'index.html')
            has_output = os.path.exists(output_path)
            projects.append({'name': name, 'has_output': has_output})
    return render_template('index.html', projects=projects)

@app.route('/delete', methods=['POST'])
def delete_project():
    project = request.form['project']
    csv_path = os.path.join(INPUT_DIR, f"{project}.csv")
    config_path = os.path.join(CONFIG_DIR, f"{project}.json")
    output_path = os.path.join(OUTPUT_DIR, project)

    for path in [csv_path, config_path, output_path]:
        if os.path.exists(path):
            if os.path.isdir(path):
                import shutil
                shutil.rmtree(path)
            else:
                os.remove(path)

    flash(f"'{project}' を削除しました。")
    return redirect(url_for('index'))

@app.route('/upload', methods=['POST'])
def upload():
    project = request.form['project']
    csv_file = request.files['csv']
    config_file = request.files['config']

    if not project or not csv_file or not config_file:
        flash('すべてのフィールドを入力してください。')
        return redirect(url_for('index'))

    csv_filename = f"{secure_filename(project)}.csv"
    json_filename = f"{secure_filename(project)}.json"

    csv_path = os.path.join(INPUT_DIR, csv_filename)
    config_path = os.path.join(CONFIG_DIR, json_filename)

    csv_file.save(csv_path)
    config_file.save(config_path)

    flash(f"'{project}' のデータと設定ファイルをアップロードしました。")
    return redirect(url_for('index'))


@app.route('/run', methods=['POST'])
def run_analysis():
    project = request.form['project']
    config_path = os.path.join(CONFIG_DIR, f"{secure_filename(project)}.json")

    if not os.path.exists(config_path):
        flash(f"設定ファイルが見つかりません: {config_path}")
        return redirect(url_for('index'))

    try:
        subprocess.run(['python', MAIN_SCRIPT, f'configs/{project}.json', '--skip-interaction'],
                       cwd=os.path.join(BASE_DIR, 'scatter/pipeline'),
                       check=True)
        flash(f"'{project}' の分析を実行しました。")
        return redirect(url_for('serve_report', project=project))  # ← 修正！
    except subprocess.CalledProcessError as e:
        flash(f"分析中にエラーが発生しました: {e}")
        return redirect(url_for('index'))

@app.route('/results/<project>/_next/<path:filename>')
def next_static_scoped(project, filename):
    static_dir = os.path.join(OUTPUT_BASE_DIR, project, 'report', '_next')
    return send_from_directory(static_dir, filename)

# 結果HTMLの表示
@app.route('/results/<project>/')
def serve_report(project):
    report_path = os.path.join(OUTPUT_BASE_DIR, project, 'report', 'index.html')
    if not os.path.exists(report_path):
        return "Report not found", 404
    with open(report_path, 'r', encoding='utf-8') as f:
        html = f.read()
    return render_template_string(html)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
