"use client"

import React from 'react';

export default function NavMenu() {

    const buttonData = [
        {
            "label": "Scan Email",
            "link": "/emailscan"
        },
        {
            "label": "AutoApply",
            "link": "/autoapply"
        },
        {
            "label": "Edit Personal Info",
            "link": "/user/settings"
        }
    ]

    return (
        <div className="flex flex-col w-[400px]">
            <hr />
            {buttonData.map(item => (
                <div key={item.label}>
                    <NavButton key={item.label} item={item} />
                    <hr />
                </div>
            ))} 
        </div>
    )
}

interface ButtonProps {
    item: {
        label: string;
        link: string;
    };
}

function NavButton({ item }: ButtonProps) {

    const handleClick = () => {
        window.location.href = item.link;
    };

    return (
        <button onClick={handleClick} className='text-left bg-gray-100 hover:bg-gray-200 w-full p-3'>
            {item.label}
        </button>
    );
}