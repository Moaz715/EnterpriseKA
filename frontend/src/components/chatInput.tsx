"use Client";

export default function ChatInput(){

    return(
        <span className="gap-4">
            <button>Add files</button>
            <input type="text" placeholder="Enter message" className="rounded-lg "/>
            <button>Send</button>
        </span>
    );
}