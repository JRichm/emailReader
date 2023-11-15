"use client"

import { useEffect, useState } from 'react';

interface ReportData {
  tableName: string;
  columnNames: string[];
  data: {};
}

interface TableData {
  tableName: string;
  columnNames: string[];
  data: {};
}

export default function Tables() {
console.log('Tables called')
  const [reportOverviewData, setReportOverviewData] = useState<ReportData[] | null>(null);
  const [error, setError] = useState<Error | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://localhost:5000/get_overview_data');
        const data = await response.json();
        console.log("data from response.json()")
        console.log(data)
        setReportOverviewData(data);
      } catch (error) {
        setError(error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  const TableElements = () => {
    console.log('TableElements called');

    if (!reportOverviewData) {
      console.log('reportOverviewData is undefined');
      return null;
    }

    console.log('reportOverviewData:', JSON.stringify(reportOverviewData));

    return (
      <div className='w-full'>
        {reportOverviewData.map((tableData) => (
          <div key={tableData.tableName}>
            <h1 className='text-2xl mb-2'>{tableData.tableName}</h1>
            <hr />
            <table className='w-full border-collapse mb-12'>
              <thead>
                <tr className='border-r border-gray-3'>
                  {tableData.columnNames && tableData.columnNames.map((columnName) => (
                    <th key={columnName} className='border-l border-b border-gray-3 font-normal bg-gray-100'>{columnName}</th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {/* Render rows based on your actual data structure */}
                {/* Example: */}
                <tr>
                  {tableData.columnNames && tableData.columnNames.map((columnName) => (
                    <td key={columnName} className='border-b border-l border-r border-gray-3'>Sample Data</td>
                  ))}
                </tr>
              </tbody>
            </table>
          </div>
        ))}
      </div>
    );
  };

  return (
    <div className='w-full ml-0'>
      {loading && <p>Loading...</p>}
      {error && <p>Error: {error.message}</p>}
      <TableElements />
    </div>
  );
}