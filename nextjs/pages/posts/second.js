import Link from 'next/link'
import Head from 'next/head'
import Container from '../../components/container'

export default function SecondPost(props) {
   return (
      <>
         <Container>
            <Head>
               <title>My second Post</title>
            </Head>
            <h1>My second Post</h1>
            <h2>
               <Link href="/">
                  <a>Home</a>
               </Link>
               <div>Next stars: {props.stars}</div>
            </h2>
         </Container>
      </>	  
   )
}

export async function getStaticProps() {
   const res = await fetch('https://api.github.com/repos/vercel/next.js');
}