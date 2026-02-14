"use client";

import { useState } from "react";
import { CampaignContent } from "@/types";

interface ReviewPanelProps {
  content: CampaignContent;
  onApprove: () => void;
  onRegenerate: (instructions: string) => void;
}

export function ReviewPanel({ content, onApprove, onRegenerate }: ReviewPanelProps) {
  /**
   * TODO:
   * 1. Display each content piece (instagram, event description, email, SMS) in its own card
   * 2. "Approve All" button -> calls onApprove()
   * 3. "Regenerate" button -> shows a text input for edit instructions, then calls onRegenerate()
   * 4. Consider making content pieces individually editable (stretch goal)
   *
   * This is the human-in-the-loop UX - make it feel intentional.
   */

  return (
    <div className="space-y-6">
      <h2 className="text-2xl font-semibold">Review Campaign Content</h2>

      {/* TODO: Content cards go here */}

      <div className="flex gap-4">
        <button
          onClick={onApprove}
          className="bg-green-600 hover:bg-green-700 text-white font-medium py-3 px-6 rounded-lg transition-colors"
        >
          Approve All
        </button>
        <button
          className="bg-gray-700 hover:bg-gray-600 text-white font-medium py-3 px-6 rounded-lg transition-colors"
        >
          Regenerate
        </button>
      </div>
    </div>
  );
}
