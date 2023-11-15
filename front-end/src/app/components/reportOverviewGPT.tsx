"use client"

// Import necessary dependencies
import React, { useEffect, useState } from 'react';

// Define interfaces
interface TableData {
  tableName: string;
  columnNames: string[];
}

interface ReportTableProps {
  data: TableData;
}

// Fetch data from the server
async function fetchOverviewData() {
  try {
    const response = await fetch('http://localhost:5000/get_overview_data');
    return await response.json();
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
}

// Main component
export default function ReportOverview() {
  const [overviewData, setOverviewData] = useState<TableData[] | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const data = await fetchOverviewData();
        setOverviewData(data);
      } catch (error) {
        setError(error);
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
      {Array.isArray(overviewData) &&
        overviewData.map((tableData) => (
          <ReportTable key={tableData.tableName} data={tableData} />
        ))}
    </div>
  );
}

// ReportTable component
function ReportTable({ data }: ReportTableProps) {
    // Conditionally render the ReportTable when data is available
    return data ? (
        <div>
            <div>
            <h1>{data.tableName}</h1>
            </div>
            <ColumnHeader names={data.columnNames} />
            <div className='bg-gray-100 m-2'>
            <table>
                {/* Table Header */}
                <thead>
                <tr>
                    {data.columnNames &&
                    data.columnNames.map((name) => (
                        <th key={name}>{name}</th>
                    ))}
                </tr>
                </thead>
                {/* Table Body - You can replace this with your actual data */}
                <tbody>
                  <tr>
                      {data.columnNames &&
                      data.columnNames.map((name) => (
                          <td key={name}>Sample Data</td>
                      ))}
                  </tr>
                </tbody>
            </table>
            </div>
        </div>
    ) : null;
}

// ColumnHeader component
const ColumnHeader = ({ names }: { names: string[] | undefined }) => {
  return (
    <div className='bg-green-200 h-fit'>
      {names &&
        names.map((name) => (
          <div key={name}>
            <p>{name}</p>
          </div>
        ))}
    </div>
  );
};