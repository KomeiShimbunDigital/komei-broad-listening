import Head from 'next/head'

type CustomTitleProps = {
  config: {
    name: string
  }
}

const CustomTitle = ({config}: CustomTitleProps) => {
  const title = config.name

  return (
    <>
      <Head>
        <title>{title}</title>
      </Head>
    </>
  )
}

export default CustomTitle
