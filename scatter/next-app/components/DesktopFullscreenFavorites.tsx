import {BookmarkCheckIcon, XIcon} from 'lucide-react'
import React from 'react'
import {ColorFunc} from '@/hooks/useClusterColor'
import {Translator} from '@/hooks/useTranslatorAndReplacements'
import {Cluster, FavoritePoint} from '@/types'

type Props = {
  favorites: FavoritePoint[]
  removeFavorite: (fav: FavoritePoint) => void
  clusters: Cluster[]
  translator: Translator
  color: ColorFunc
  onlyCluster?: string
  onClose: () => void
}

export function DesktopFullscreenFavorites({
  favorites,
  removeFavorite,
  clusters,
  translator,
  color,
  onlyCluster,
  onClose
}: Props) {
  return (
    <div
      className="absolute top-0 right-0 w-[400px] p-4 bg-gray-100 overflow-y-auto z-10 h-full shadow-md"
    >
      <div className="flex justify-between items-center mb-4 h-[32px]">
        <h2 className="text-md font-bold">
          {translator.t('お気に入り一覧')}
        </h2>
        <button onClick={onClose}>
          <XIcon/>
        </button>
      </div>
      {favorites.length === 0 ? (
        <p>{translator.t('お気に入りがありません')}</p>
      ) : (
        <ul>
          {favorites.map((fav) => {
            // クラスタ情報を取得
            const cluster = clusters.find((c) => c.cluster_id === fav.cluster_id)
            return (
              <li
                key={fav.arg_id}
                className="mb-2 p-2 bg-white rounded shadow flex flex-col"
              >
                <div className="flex items-center justify-between">
                  {/* クラスタラベル */}
                  <h3
                    className="font-semibold text-md"
                    style={{
                      color: cluster ? color(cluster.cluster_id, onlyCluster) : '#000',
                    }}
                  >
                    {translator.t(cluster?.cluster || 'クラスタ')}
                  </h3>

                  {/* お気に入りボタン */}
                  <button
                    onClick={() => removeFavorite(fav)}
                    className="text-amber-500 text-lg focus:outline-none ml-2"
                  >
                    <BookmarkCheckIcon/>
                  </button>
                </div>

                {/* 引用部分を100文字に制限 */}
                <p className="text-md text-gray-700 mt-1">
                  {truncateText(fav.argument, 100)}
                </p>
              </li>
            )
          })}
        </ul>
      )}
    </div>
  )
}

function truncateText(text: string, maxLength: number) {
  if (text.length <= maxLength) return text
  return text.slice(0, maxLength) + '...'
}
