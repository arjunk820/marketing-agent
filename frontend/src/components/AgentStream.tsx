"use client";

import { useEffect, useState } from "react";
import { AgentStreamEvent } from "@/types";

interface AgentStreamProps {
  campaignId: string;
  onComplete: () => void;
}

const AGENT_STEPS = [
  { id: "research", label: "Researching venue & scene" },
  { id: "audience", label: "Profiling target audience" },
  { id: "content", label: "Generating marketing content" },
];

export function AgentStream({ campaignId, onComplete }: AgentStreamProps) {
  /**
   * TODO:
   * 1. Connect to SSE stream via subscribeToCampaignStream() from lib/api.ts
   * 2. Track which steps are pending/running/complete in local state
   * 3. Update step status as SSE events arrive
   * 4. Call onComplete() when all steps finish (stream closes)
   * 5. Clean up EventSource on unmount
   *
   * Render a vertical stepper/timeline showing each agent node's progress.
   */

  return (
    <div className="space-y-4">
      <h2 className="text-2xl font-semibold">Generating Campaign...</h2>

      <div className="space-y-3">
        {AGENT_STEPS.map((step) => (
          <div key={step.id} className="flex items-center gap-3 p-4 bg-gray-900 rounded-lg">
            {/* TODO: Show status icon (spinner/checkmark) based on step state */}
            <span className="text-gray-400">{step.label}</span>
          </div>
        ))}
      </div>
    </div>
  );
}
