"use client";

import { useState } from "react";
import { EventBrief } from "@/types";

interface EventBriefFormProps {
  onSubmit: (brief: EventBrief) => void;
}

export function EventBriefForm({ onSubmit }: EventBriefFormProps) {
  /**
   * TODO:
   * 1. Create controlled form state for each EventBrief field
   * 2. venue_type: dropdown with options (nightclub, rooftop, lounge, warehouse, other)
   * 3. genre: dropdown (RnB, House, Hip-Hop, Afrobeats, Techno, Other)
   * 4. vibe: free-text input with placeholder examples
   * 5. dj_name & additional_notes: optional fields
   * 6. On submit: call onSubmit(brief) with the form data
   * 7. Add basic validation (required fields)
   */

  return (
    <form className="space-y-6">
      <h2 className="text-2xl font-semibold">Create Campaign</h2>

      {/* TODO: Add form fields here */}

      <button
        type="submit"
        className="w-full bg-purple-600 hover:bg-purple-700 text-white font-medium py-3 px-6 rounded-lg transition-colors"
      >
        Generate Campaign
      </button>
    </form>
  );
}
