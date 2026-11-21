"use client";

import ChatSidebar from "@/src/components/chatSidebar";
import ChatInput from "@/src/components/chatInput";
import { useState } from "react";

type Message = {
    id: number;
    content: string;
    role: "user" | "assistant";
    files: File[];
};

export default function Chat() {
    const [messages, setMessages] = useState<Message[]>([]);

    const handleSubmit = (message: string, files: File[]) => {
        const newMessage: Message = {
            id: Date.now(),
            content: message,
            role: "user",
            files,
        };

        setMessages((prev) => [...prev, newMessage]);
    };

    return (
        <main>
            <ChatSidebar />

            <section>
                <header>
                    <h1>Enterprise Knowledge Assistant</h1>
                </header>

                <div>
                    {messages.map((msg) => (
                        <div key={msg.id}>
                            <p>{msg.role}</p>
                            <p>{msg.content}</p>

                            {msg.files.map((file, index) => (
                                <p key={`${file.name}-${index}`}>
                                    {file.name}
                                </p>
                            ))}
                        </div>
                    ))}
                </div>

                <ChatInput onSend={handleSubmit} />
            </section>
        </main>
    );
}