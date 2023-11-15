import Image from 'next/image'
import MainHeader from './components/header'
import NavMenu from './components/navMenu'
import ReportOverview from './components/reportOverview'

export default function Home() {
  return (
    <main>
        <MainHeader />
        <div className='flex flex-row justify-center'>
          <NavMenu />
          <ReportOverview />
        </div>
    </main>
  )
}
