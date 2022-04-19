import Link from 'next/link'
import Head from 'next/head'

function HomePage() {
   return (
      <>
         <head>
            <title>This is my first nextjs project</title>
         </head>
         <div>Welcome to Next.js!</div>
         <Link href="/posts/first"><a>First Post</a></Link>
         <img src='/banner.jpeg' alt='A banner'/>
      </>	    
   )
}

export default HomePage