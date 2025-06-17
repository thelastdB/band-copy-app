prompt_templates = {
    "Show Announcement": """
You're writing in the voice of an indie alt-country band.

Here are past show announcement examples:
{examples}

Now write a new {mood} show announcement. Make it conversational and engaging. Include key details:
{details}. Avoid cliches. Nothing too on the nose about country music.
""",

    "New Music Promo": """
You're writing a social media post to promote a new single from an indie alt-country band.

Here are past promo examples:
{examples}

Write a {mood}, punchy and emotional post about the new release. Include the following info:
{details}. Avoid cliches. Nothing too on the nose about country music.
""",

    "Email Blurb": """
You're writing a newsletter blurb from an indie alt-country band to fans.

Here are past email examples:
{examples}

Write a {mood}, direct blurb that includes:
{details}. Avoid cliches. Nothing too on the nose about country music.
"""
}