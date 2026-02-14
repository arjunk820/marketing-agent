import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Fantasia - Event Marketing Agent",
  description: "AI-powered event marketing campaign generator",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
