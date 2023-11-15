import Image from 'next/image'
import MainHeader from './components/header'
import NavMenu from './components/navMenu'
import Tables from './components/tables'

export default function Home() {
  return (
    <div className='flex flex-col'>
        <MainHeader />
        <div className='flex flex-row gap-12 m-12'>
          <NavMenu />
          <Tables />
        </div>
    </div>
  )
}
