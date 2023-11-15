'use client'

import { useEffect, useState } from 'react';

interface ReportData {
    tableName: string;
    columnNames: string[];
}

interface ReportTableProps {
    data: ReportData;
}
export default function ReportOverview() {

    const [reportOverviewData, setReportOverviewData] = useState<ReportData[] | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<Error | null>(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch('http://localhost:5000/get_overview_data');
                const data = await response.json();
                setReportOverviewData(data);
            } catch (error) {
                if (error instanceof Error) {
                    setError(error);
                } else {
                    console.error('Unexpected error type:', error);
                }
            } finally {
                setLoading(false);
            }
        };
    
        fetchData();
    }, []);

    return (
        <div>
            {loading && <p>Loading...</p>}
            {error && <p>Error: {error.message}</p>}
            {Array.isArray(reportOverviewData) && reportOverviewData.map(tableData => (
            <ReportTable key={tableData.tableName} data={tableData} />
            ))}
        </div>
    );
}

function ReportTable(props: ReportTableProps) {
    const { data } = props;

    console.log(data)

    // Conditionally render the ReportTable when data is available
    return data ? (
        <div>
            <div>
                <h1>{data.tableName}</h1>
            </div>
            <ColumnHeader names={data.columnNames} />
            <div className='bg-gray-100 m-2'>
                <pre>{JSON.stringify(data, null, '\t')}</pre>
            </div>
        </div>
    ) : null;
}

const ColumnHeader = ({ names }: { names: string[] | undefined }) => {
    return (
        <div className='bg-green-200 h-fit'>
        {names && names.map((name) => (
            <div key={name}>
                <p>fart{name}</p>
            </div>
        ))}
        </div>
    );
}