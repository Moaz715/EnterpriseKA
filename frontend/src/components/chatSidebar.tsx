"use client";

export default function ChatSidebar() {

    return (
        <aside className="bg-blue-800 text-amber-50 flex h-screen flex-col">
            <div className="mt-4">
                <h1>Knowledge AI</h1>
                <button>New Chat</button>
                <div className="flex">
                    <input type="text" placeholder="Search Chats" />
                    <button>Search</button>
                </div>
            </div>

            <div className="mt-4">
                Chats
            </div>

            <div className="mt-auto">
                <button>Settings</button>
                <p>Workspace Account</p>
            </div>
        </aside>

    );
}