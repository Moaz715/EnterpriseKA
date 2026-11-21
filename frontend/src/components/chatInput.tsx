"use client";

import { useState } from "react";

type ChatInputProps = {
    onSend: (message: string, files: File[]) => void;
};

export default function ChatInput({ onSend }: ChatInputProps) {
    const [files, setFiles] = useState<File[]>([]);
    const [message, setMessage] = useState("");

    function handleSubmit(e: React.SubmitEvent<HTMLFormElement>) {
        e.preventDefault();

        if (!message.trim() && files.length === 0) return;

        onSend(message, files);

        setMessage("");
        setFiles([]);
    }

    return (
        <form
            onSubmit={handleSubmit}
            className="rounded-2xl border border-slate-300 bg-white p-3 shadow-sm"
        >
            
            {files.length > 0 && (
                <div className="mb-3 flex flex-wrap gap-2">
                    {files.map((file, index) => (
                        <div
                            key={`${file.name}-${index}`}
                            className="rounded-lg bg-slate-100 px-3 py-2 text-sm text-slate-700"
                        >
                            {file.name}
                        </div>
                    ))}
                </div>
            )}

            
            <textarea
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                placeholder="Ask anything about your organization's knowledge..."
                className="w-full resize-none border-none bg-transparent p-2 text-sm outline-none placeholder:text-slate-400"
            />

            
            <div className="mt-2 flex items-center justify-between">
                <label className="cursor-pointer rounded-lg px-3 py-2 text-sm text-slate-950 transition hover:bg-slate-100">
                    Attach files

                    <input
                        type="file"
                        multiple
                        className="hidden"
                        onChange={(e) =>
                            setFiles((prev) => [
                                ...prev,
                                ...Array.from(e.target.files ?? []),
                            ])
                        }
                    />
                </label>

                <button
                    type="submit"
                    disabled={!message.trim() && files.length === 0}
                    className="rounded-lg bg-slate-900 px-4 py-2 text-sm font-medium text-white transition hover:bg-slate-700 disabled:cursor-not-allowed disabled:bg-slate-300"
                >
                    Send
                </button>
            </div>
        </form>
    );
}