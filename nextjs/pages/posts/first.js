import Link from 'next/link'
import Head from 'next/head'
import Container from '../../components/container'

export default function FirstPost() {
   return (
      <>
            <head>
               <title>
                  This is the first post!
               </title>
            </head>
 
               <div>
            <h1>My First Post</h1>
            <h2>
               <Link href="/">
                  <a>Home</a>
               </Link>
               <img src="/banner.jpeg" alt="TutorialsPoint Logo" />
            </h2>
            </div>


      </>
   )
}