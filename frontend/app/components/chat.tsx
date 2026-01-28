"use client";
import React, { useState, useRef, useEffect } from "react";
import { useWebSocket, Message } from "../lib/useWebsocket";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { oneDark } from "react-syntax-highlighter/dist/esm/styles/prism";

function isProbablyPython(text: string) {
  // detect fenced codeblocks with python or simple heuristics
  if (/^```(?:python)?/im.test(text)) return true;
  if (/\b(def |import |from |class )/.test(text) && /\n\s+/.test(text)) return true;
  return false;
}

export default function Chat() {

  const { messages, sendMessage, sendFirstMessage, status } = useWebSocket(
    "ws://localhost:8765"
  );

  const [text, setText] = useState("");
  const inputRef = useRef<HTMLInputElement | null>(null);
  // track whether we've sent the initial "hello" for the current connection
  const connectionHelloSent = useRef(false);

  useEffect(() => {
    inputRef.current?.focus();
  }, []);

  useEffect(() => {
    if (status === "open" && !connectionHelloSent.current) {
      sendFirstMessage("hello");
      connectionHelloSent.current = true;
    }
  }, [status, sendMessage]);

  const submit = (e?: React.FormEvent) => {
    e?.preventDefault();
    const trimmed = text.trim();
    if (!trimmed) return;
    sendMessage(trimmed);
    setText("");
  };

  return (
    <div className="flex h-screen flex-col bg-zinc-50 dark:bg-black">
      <header className="p-4 border-b border-gray-200 dark:border-gray-800">
        <div className="max-w-3xl mx-auto flex items-center justify-between">
          <h1 className="text-lg font-semibold">AI Programmers Team</h1>
          <span className="text-sm text-gray-500">WS: {status}</span>
        </div>
      </header>

      <main className="flex-1 overflow-hidden">
        <div className="max-w-3xl mx-auto h-full flex flex-col">
          <div
            id="chat-window"
            className="flex-1 overflow-y-auto p-6 space-y-4 bg-white dark:bg-black"
          >
            {messages.map((m) => (
              <div
                className={`flex ${
                  m.side === "me" ? "justify-end" : "justify-start"
                }`}
              >
                <div
                  className={`max-w-[70%] px-4 py-2 rounded-lg ${
                    m.side === "me"
                      ? "bg-blue-600 text-white rounded-br-none"
                      : "bg-gray-200 text-gray-900 rounded-bl-none dark:bg-gray-800 dark:text-gray-100"
                  }`}
                >
                  {m.side === "other" &&
                    <div className="text-xs text-gray-500 mb-1">{m.role}</div>
                  }

                  {isProbablyPython(m.message) ? (
                    <SyntaxHighlighter language="python" style={oneDark} wrapLongLines>
                      {m.message.replace(/^```(?:python)?\n?|```$/g, "")}
                    </SyntaxHighlighter>
                  ) : (
                    <>{m.message}</>
                  )}
                </div>
              </div>
            ))}
          </div>

          <form
            onSubmit={submit}
            className="border-t border-gray-200 dark:border-gray-800 p-4 bg-white dark:bg-black"
          >
            <div className="max-w-3xl mx-auto flex gap-2">
              <input
                ref={inputRef}
                value={text}
                onChange={(e) => setText(e.target.value)}
                placeholder="Type a message..."
                className="flex-1 rounded-full border border-gray-300 px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400 dark:bg-gray-900 dark:border-gray-700"
                onKeyDown={(e) => {
                  if (e.key === "Enter" && !e.shiftKey) {
                    submit();
                  }
                }}
              />
              <button
                type="submit"
                className="rounded-full bg-blue-600 px-4 py-2 text-white hover:bg-blue-700 disabled:opacity-50"
                disabled={!text.trim()}
              >
                Send
              </button>
            </div>
          </form>
        </div>
      </main>
    </div>
  );
}