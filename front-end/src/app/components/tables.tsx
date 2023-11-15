"use client"

import '../styles/tables.css'
import { useEffect, useState } from 'react';

interface ReportData {
    tableName: string;
    columnNames: string[];
    data: { [key: string]: any }[]; // Replace 'any' with the actual type of your data
} 

interface TableData {
    tableName: string;
    columnNames: string[];
    data: { [key: string]: any }[]; // Replace 'any' with the actual type of your data
}

export default function Tables() {
    console.log('Tables called');
    const [reportOverviewData, setReportOverviewData] = useState<ReportData[] | null>(null);
    const [error, setError] = useState<Error | null>(null);
    const [loading, setLoading] = useState(true);
    const [selectedRows, setSelectedRows] = useState<{ [key: string]: boolean }>({});
    const [selectAll, setSelectAll] = useState(false);
    const [selectedRowsWithIndex, setSelectedRowsWithIndex] = useState<{ [key: string]: boolean }>({});

    // Toggle the selection of a specific row
    const toggleRowSelection = (tableIndex: number, rowIndex: number) => {
        setSelectedRowsWithIndex((prevSelectedRows) => ({
            ...prevSelectedRows,
            [`${tableIndex}-${rowIndex}`]: !prevSelectedRows[`${tableIndex}-${rowIndex}`],
        }));
    };

    // Toggle the selection of all rows
    const toggleSelectAll = () => {
        setSelectAll((prevSelectAll) => !prevSelectAll);
        setSelectedRows((prevSelectedRows) => {
            const newSelectedRows: { [key: string]: boolean } = {};
    
            // Set all rows to the new value of selectAll
            Object.keys(prevSelectedRows).forEach((key) => {
                // Assuming that the keys are in the format 'tableIndex-rowIndex'
                newSelectedRows[key] = !selectAll;
            });
    
            return newSelectedRows;
        });
    };
  
    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch('http://localhost:5000/get_overview_data');
                const data: ReportData[] = await response.json();
                console.log("data from response.json()");
                console.log(data);
        
                // Initialize selectedRowsWithIndex with all rows selected
                const initialSelectedRowsWithIndex: { [key: string]: boolean } = {};
                data.forEach((tableData, tableIndex) => {
                    // Check if 'data' is not null before iterating
                    if (tableData.data) {
                        tableData.data.forEach((_, rowIndex) => {
                            initialSelectedRowsWithIndex[`${tableIndex}-${rowIndex}`] = true;
                        });
                    }
                });
        
                setReportOverviewData(data);
                setSelectedRowsWithIndex(initialSelectedRowsWithIndex);
            } catch (error) {
                setError(error as Error);
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
    
        return (
            <div className='w-full'>
                {reportOverviewData.map((tableData, tableIndex) => (
                    <div key={tableData.tableName}>
                        <div className='flex flex-row justify-between place-items-center'>
                            <h1 className='text-4xl m-2'>{tableData.tableName}</h1>
                            <div className='flex space-x-2'>
                                <input
                                    type='button'
                                    value='Refresh'
                                    className='transition-all bg-green-300px-3 h-8 mx-2 px-4 rounded-md text-green-700 border bg-green-200 border-green-400 hover:cursor-pointer hover:bg-green-400 hover:text-green-100' >
                                </input>
                                {tableData.tableName === 'Unopened Job Links' && (
                                    <input
                                        type='button'
                                        value='Auto Apply'
                                        className='transition-all bg-blue-300 px-3 h-8 mx-2 rounded-md text-blue-700 border border-blue-400 hover:cursor-pointer hover:bg-blue-400 hover:text-blue-100'
                                        onClick={() => handleAutoApply(tableData, selectedRows)}
                                ></input>
                            )}
                            </div>
                        </div>
                        <hr />
                        <table className='w-full border-collapse mb-12'>
                            <thead>
                                <tr className='border-r border-gray-3'>
                                    { tableData.tableName === 'Unopened Job Links' && (
                                        <th className='border-l border-b border-gray-3 font-normal bg-neutral-500 text-zinc-100 p-2 px-5'>
                                            <input type='checkbox'checked={selectAll} onChange={toggleSelectAll} />
                                        </th>
                                    )}
                                    {tableData.columnNames &&
                                    tableData.columnNames.map((columnName) => (
                                        <th key={columnName} className={`border-l border-b border-gray-3 font-normal bg-neutral-500 text-zinc-100 p-2 ${columnName}`} >
                                            {columnName}
                                        </th>
                                    ))}
                                </tr>
                            </thead>
                            <tbody>
                                {tableData.data && tableData.data.map((item, index) => (
                                    <tr key={index} className={`${index % 2 === 0 ? 'table-row-alt' : ''}`} >
                                        {tableData.tableName === 'Unopened Job Links' && (
                                            <td className='flex justify-center m-2'>
                                                <input type='checkbox' className='' checked={selectedRows[`${tableIndex}-${index}`] ?? false} onChange={() => toggleRowSelection(tableIndex, index)} />
                                            </td>
                                        )}
                                        {tableData.columnNames.map((columnName) => (
                                            <td key={columnName} className='text-center'>
                                                {columnName === 'link' ? (
                                                    <a href={item[columnName]} target='_blank' rel='noopener noreferrer' className='text-blue-800 hover:text-blue-300' >
                                                        <span title={item[columnName]}>
                                                            {item[columnName].slice(12, 51)}...
                                                        </span>
                                                    </a>
                                                ) : (
                                                    item[columnName]
                                                )}
                                            </td>
                                        ))}
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                ))}
            </div>
        );
    };

    const handleAutoApply = (tableData: ReportData, selectedRows: { [key: string]: boolean }) => {
        // Add your logic for auto applying using selectedRows
        console.log('Auto Apply clicked for JobLinks');
        console.log('Table Data:', tableData);
        console.log('Table Index:', tableIndex);
        console.log('Row Index:', rowIndex);
    };

    return (
        <div className='w'>
            {loading && <p>Loading...</p>}
            {error && <p>Error: {error.message}</p>}
            <TableElements />
        </div>
    );
}