import { useEffect, useRef, useState } from "react";

export type Message = {
  message: string;
  role: string;
  side?: undefined | "me" | "other";
};

export function useWebSocket(url: string) {
  const wsRef = useRef<WebSocket | null>(null);
  const [messages, setMessages] = useState<Message[]>([]);
  const [status, setStatus] = useState<string>("disconnected");

  useEffect(() => {
    const ws = new WebSocket(url);
    wsRef.current = ws;
    setStatus("connecting");

    const message: Message = { 
      message: "Cześć, tu zespół programistów AI. Wpisz poniżej swój prompt, a zobaczysz, jak kod jest generowany, testowany i dostarczany do Ciebie!", 
      role: "AI Programmers Team", 
      side: "other" 
    };

    setMessages((prev) => [...prev, message]);

    ws.addEventListener("open", () => {
      setStatus("open");
    });

    ws.addEventListener("message", (event) => {
      try {
        const data = JSON.parse(event.data);
        if (data && (data.type === "message" || data.message)) {
          const msg: Message = {
            message: String(data.message ?? event.data),
            role: String(data.role ?? "Unknown"),
            side: "other",
          };
          setMessages((prev) => [...prev, msg]);
        } else {
          setMessages((prev) => [
            ...prev,
            {
              message: String(event.data),
              role: "other",
            } as Message,
          ]);
        }
      } catch {
        setMessages((prev) => [
          ...prev,
          { message: String(event.data), role: "other" } as Message,
        ]);
      }
    });

    ws.addEventListener("close", () => {
      setStatus("closed");
    });

    ws.addEventListener("error", () => {
      setStatus("error");
    });

    return () => {
      ws.close();
      wsRef.current = null;
    };
  }, [url]);

  const sendMessage = (text: string) => {
    const msg: Message = { message: text, role: "GUI", side: "me" };
    setMessages((prev) => [...prev, msg]);

    const payload = JSON.stringify({ message: text, role: "GUI" });
    if (wsRef.current && wsRef.current.readyState === WebSocket.OPEN) {
      wsRef.current.send(payload);
    } else {
      console.warn("WebSocket not open - message not sent over network", payload);
    }
  };

  const sendFirstMessage = (text: string) => {
    const msg: Message = { message: text, role: "GUI", side: "me" };

    const payload = JSON.stringify({ message: text, role: "GUI" });
    if (wsRef.current && wsRef.current.readyState === WebSocket.OPEN) {
      wsRef.current.send(payload);
    } else {
      console.warn("WebSocket not open - message not sent over network", payload);
    }
  };

  return { messages, sendMessage, sendFirstMessage,status };
}