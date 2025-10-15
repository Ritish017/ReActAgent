from langchain.callbacks.base import BaseCallbackHandler

class AgentCallbackHandler(BaseCallbackHandler):
    def on_llm_start(self, serialized, prompts, *, run_id, parent_run_id = None, tags = None, metadata = None, **kwargs):
        return super().on_llm_start(serialized, prompts, run_id=run_id, parent_run_id=parent_run_id, tags=tags, metadata=metadata, **kwargs)

    def on_llm_end(self, response, *, run_id, parent_run_id = None, tags = None, metadata = None, **kwargs):
        return super().on_llm_end(response, run_id=run_id, parent_run_id=parent_run_id, tags=tags, metadata=metadata, **kwargs)
