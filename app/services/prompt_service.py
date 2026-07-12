from app.prompts.chat_prompt import CHAT_PROMPT


class PromptService:
    """
    Responsible for building prompts for the LLM.
    """

    @staticmethod
    def build_prompt(
        question: str,
        context: str,
    ) -> str:
        """
        Build the final prompt for the language model.

        Args:
            question: User question.
            context: Retrieved context.

        Returns:
            Formatted prompt string.
        """

        return CHAT_PROMPT.format(
            context=context,
            question=question,
        )