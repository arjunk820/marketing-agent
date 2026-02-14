export interface EventBrief {
  venue_name: string;
  venue_type: "nightclub" | "rooftop" | "lounge" | "warehouse" | "other";
  city: string;
  date: string;
  genre: string;
  vibe: string;
  dj_name?: string;
  additional_notes?: string;
}

export interface CampaignContent {
  instagram_caption: string;
  event_description: string;
  email_blast: { subject: string; body: string };
  sms_teaser: string;
}

export interface Campaign {
  id: string;
  status: "processing" | "awaiting_review" | "approved" | "exported";
  event_brief: EventBrief;
  research?: Record<string, unknown>;
  audience_profile?: Record<string, unknown>;
  content?: CampaignContent;
  final_campaign?: Record<string, unknown>;
}

export interface AgentStreamEvent {
  node: string;
  status: "running" | "complete" | "error";
  preview?: string;
}
