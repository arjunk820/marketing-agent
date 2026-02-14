import { EventBrief, Campaign } from "@/types";

const API_BASE = "http://localhost:8000";

export async function createCampaign(brief: EventBrief): Promise<{ campaign_id: string }> {
  /**
   * TODO:
   * 1. POST to /campaigns with the event brief
   * 2. Return the campaign_id from the response
   */
  throw new Error("Not implemented");
}

export function subscribeToCampaignStream(
  campaignId: string,
  onEvent: (event: { node: string; status: string; preview?: string }) => void
): EventSource {
  /**
   * TODO:
   * 1. Create an EventSource connection to /campaigns/{id}/stream
   * 2. Parse incoming SSE messages and call onEvent
   * 3. Return the EventSource so the caller can close it
   */
  throw new Error("Not implemented");
}

export async function submitReview(
  campaignId: string,
  feedback: string
): Promise<Campaign> {
  /**
   * TODO:
   * 1. POST to /campaigns/{id}/review with { feedback }
   * 2. Return the updated campaign
   */
  throw new Error("Not implemented");
}

export async function getCampaign(campaignId: string): Promise<Campaign> {
  /**
   * TODO:
   * 1. GET /campaigns/{id}
   * 2. Return the campaign data
   */
  throw new Error("Not implemented");
}
