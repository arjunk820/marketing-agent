"use client";

import { useState } from "react";
import { EventBriefForm } from "@/components/EventBriefForm";
import { AgentStream } from "@/components/AgentStream";
import { ReviewPanel } from "@/components/ReviewPanel";
import { CampaignExport } from "@/components/CampaignExport";
import { Campaign } from "@/types";

export default function Home() {
  const [campaignId, setCampaignId] = useState<string | null>(null);
  const [campaign, setCampaign] = useState<Campaign | null>(null);

  /**
   * TODO:
   * 1. Show EventBriefForm when no campaign exists
   * 2. After form submit -> show AgentStream while agents run
   * 3. When agents finish -> show ReviewPanel for human-in-the-loop
   * 4. After approval -> show CampaignExport with final output
   *
   * Use campaign.status to determine which component to render:
   *   - "processing" -> AgentStream
   *   - "awaiting_review" -> ReviewPanel
   *   - "approved" / "exported" -> CampaignExport
   */

  return (
    <main className="min-h-screen bg-gray-950 text-white">
      <div className="max-w-4xl mx-auto px-4 py-12">
        <h1 className="text-4xl font-bold mb-8">Fantasia</h1>
        <p className="text-gray-400 mb-12">AI-powered event marketing campaigns</p>

        {/* TODO: Render components based on campaign state */}
      </div>
    </main>
  );
}
