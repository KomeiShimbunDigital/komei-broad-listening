import showdown from 'showdown'

const converter = new showdown.Converter()

const CustomIntroduction = (props: any) => {
  const {override, config} = props

  if (!override) {
    // 元のコードを使用
    if (config.intro) {
      return (
        <div className="m-auto mb-4 text-justify">
          <h3 className="font-bold mt-6">分析に関する概要</h3>
          <div
            className="italic"
            dangerouslySetInnerHTML={{
              __html: converter.makeHtml(config.intro),
            }}
          />
          <div className="mt-6">
            <h3 className="font-bold">動作環境</h3>
            <p>
              本ページを快適にご覧いただくには横幅1200px以上の環境が必要です。スマートフォンをご利用の場合、全画面地図は画面を横向きにしてご利用ください。
            </p>
          </div>
        </div>
      )
    }
    return null
  }
  return <div className="max-w-xl m-auto mb-4 text-justify">{override}</div>
}

export default CustomIntroduction
