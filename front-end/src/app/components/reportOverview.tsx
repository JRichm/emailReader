export default async function ReportOverview() {

    const reportOverviewData = await fetch('http://localhost:5000/get_overview_data')

    return(
        <div>
            <ReportTable />
        </div>
    )
}

function ReportTable() {
    return(
        <div>

        </div>
    ) 
}
