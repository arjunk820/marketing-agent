"use client";

import { Campaign } from "@/types";

interface CampaignExportProps {
  campaign: Campaign;
}

export function CampaignExport({ campaign }: CampaignExportProps) {
  /**
   * TODO:
   * 1. Display the final approved campaign in a clean, presentable layout
   * 2. Show each content piece with a "Copy" button
   * 3. Add a "Copy All" button that copies everything
   * 4. Optional: "Download as JSON" button for the full campaign object
   */

  return (
    <div className="space-y-6">
      <h2 className="text-2xl font-semibold">Campaign Ready</h2>

      {/* TODO: Final campaign display with copy buttons */}
    </div>
  );
}
