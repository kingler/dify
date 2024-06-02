# Project Tree Structure

```
├── AUTHORS
├── CONTRIBUTING.md
├── CONTRIBUTING_CN.md
├── CONTRIBUTING_JA.md
├── LICENSE
├── MABOS-Multi-Agent Business Operating System.md
├── [[Makefile]]
├── [[NetworkX.md]]
├── [[Owlready2.md]]
├── README.md
├── README_CN.md
├── README_ES.md
├── README_FR.md
├── README_JA.md
├── README_KL.md
├── README_KR.md
├── agents_state_machine.plantuml
├── api
│   ├── Dockerfile
│   ├── README.md
│   ├── app.py
│   ├── commands.py
│   ├── config.py
│   ├── constants
│   │   ├── __init__.py
│   │   ├── languages.py
│   │   ├── model_template.py
│   │   └── recommended_apps.json
│   ├── controllers
│   │   ├── __init__.py
│   │   ├── console
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apikey.py
│   │   │   ├── app
│   │   │   │   ├── __init__.py
│   │   │   │   ├── advanced_prompt_template.py
│   │   │   │   ├── agent.py
│   │   │   │   ├── annotation.py
│   │   │   │   ├── app.py
│   │   │   │   ├── audio.py
│   │   │   │   ├── completion.py
│   │   │   │   ├── conversation.py
│   │   │   │   ├── error.py
│   │   │   │   ├── generator.py
│   │   │   │   ├── message.py
│   │   │   │   ├── model_config.py
│   │   │   │   ├── site.py
│   │   │   │   ├── statistic.py
│   │   │   │   ├── workflow.py
│   │   │   │   ├── workflow_app_log.py
│   │   │   │   ├── workflow_run.py
│   │   │   │   ├── workflow_statistic.py
│   │   │   │   └── wraps.py
│   │   │   ├── auth
│   │   │   │   ├── activate.py
│   │   │   │   ├── data_source_oauth.py
│   │   │   │   ├── login.py
│   │   │   │   └── oauth.py
│   │   │   ├── billing
│   │   │   │   ├── __init__.py
│   │   │   │   └── billing.py
│   │   │   ├── datasets
│   │   │   │   ├── data_source.py
│   │   │   │   ├── datasets.py
│   │   │   │   ├── datasets_document.py
│   │   │   │   ├── datasets_segments.py
│   │   │   │   ├── error.py
│   │   │   │   ├── file.py
│   │   │   │   └── hit_testing.py
│   │   │   ├── error.py
│   │   │   ├── explore
│   │   │   │   ├── audio.py
│   │   │   │   ├── completion.py
│   │   │   │   ├── conversation.py
│   │   │   │   ├── error.py
│   │   │   │   ├── installed_app.py
│   │   │   │   ├── message.py
│   │   │   │   ├── parameter.py
│   │   │   │   ├── recommended_app.py
│   │   │   │   ├── saved_message.py
│   │   │   │   ├── workflow.py
│   │   │   │   └── wraps.py
│   │   │   ├── extension.py
│   │   │   ├── feature.py
│   │   │   ├── init_validate.py
│   │   │   ├── ping.py
│   │   │   ├── setup.py
│   │   │   ├── tag
│   │   │   │   └── tags.py
│   │   │   ├── version.py
│   │   │   ├── workspace
│   │   │   │   ├── __init__.py
│   │   │   │   ├── account.py
│   │   │   │   ├── error.py
│   │   │   │   ├── members.py
│   │   │   │   ├── model_providers.py
│   │   │   │   ├── models.py
│   │   │   │   ├── tool_providers.py
│   │   │   │   └── workspace.py
│   │   │   └── wraps.py
│   │   ├── files
│   │   │   ├── __init__.py
│   │   │   ├── image_preview.py
│   │   │   └── tool_files.py
│   │   ├── inner_api
│   │   │   ├── __init__.py
│   │   │   ├── workspace
│   │   │   │   ├── __init__.py
│   │   │   │   └── workspace.py
│   │   │   └── wraps.py
│   │   ├── mabos_router.py
│   │   ├── service_api
│   │   │   ├── __init__.py
│   │   │   ├── app
│   │   │   │   ├── __init__.py
│   │   │   │   ├── app.py
│   │   │   │   ├── audio.py
│   │   │   │   ├── completion.py
│   │   │   │   ├── conversation.py
│   │   │   │   ├── error.py
│   │   │   │   ├── file.py
│   │   │   │   ├── message.py
│   │   │   │   └── workflow.py
│   │   │   ├── dataset
│   │   │   │   ├── __init__.py
│   │   │   │   ├── dataset.py
│   │   │   │   ├── document.py
│   │   │   │   ├── error.py
│   │   │   │   └── segment.py
│   │   │   ├── index.py
│   │   │   └── wraps.py
│   │   └── web
│   │       ├── __init__.py
│   │       ├── app.py
│   │       ├── audio.py
│   │       ├── completion.py
│   │       ├── conversation.py
│   │       ├── error.py
│   │       ├── feature.py
│   │       ├── file.py
│   │       ├── message.py
│   │       ├── passport.py
│   │       ├── saved_message.py
│   │       ├── site.py
│   │       ├── workflow.py
│   │       └── wraps.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── agent
│   │   │   ├── __init__.py
│   │   │   ├── base_agent_runner.py
│   │   │   ├── cot_agent_runner.py
│   │   │   ├── cot_chat_agent_runner.py
│   │   │   ├── cot_completion_agent_runner.py
│   │   │   ├── entities.py
│   │   │   ├── fc_agent_runner.py
│   │   │   └── output_parser
│   │   │       └── cot_output_parser.py
│   │   ├── app
│   │   │   ├── __init__.py
│   │   │   ├── app_config
│   │   │   │   ├── __init__.py
│   │   │   │   ├── base_app_config_manager.py
│   │   │   │   ├── common
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   └── sensitive_word_avoidance
│   │   │   │   │       ├── __init__.py
│   │   │   │   │       └── manager.py
│   │   │   │   ├── easy_ui_based_app
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── agent
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   └── manager.py
│   │   │   │   │   ├── dataset
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   └── manager.py
│   │   │   │   │   ├── model_config
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── converter.py
│   │   │   │   │   │   └── manager.py
│   │   │   │   │   ├── prompt_template
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   └── manager.py
│   │   │   │   │   └── variables
│   │   │   │   │       ├── __init__.py
│   │   │   │   │       └── manager.py
│   │   │   │   ├── entities.py
│   │   │   │   ├── features
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── file_upload
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   └── manager.py
│   │   │   │   │   ├── more_like_this
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   └── manager.py
│   │   │   │   │   ├── opening_statement
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   └── manager.py
│   │   │   │   │   ├── retrieval_resource
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   └── manager.py
│   │   │   │   │   ├── speech_to_text
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   └── manager.py
│   │   │   │   │   ├── suggested_questions_after_answer
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   └── manager.py
│   │   │   │   │   └── text_to_speech
│   │   │   │   │       ├── __init__.py
│   │   │   │   │       └── manager.py
│   │   │   │   └── workflow_ui_based_app
│   │   │   │       ├── __init__.py
│   │   │   │       └── variables
│   │   │   │           ├── __init__.py
│   │   │   │           └── manager.py
│   │   │   ├── apps
│   │   │   │   ├── README.md
│   │   │   │   ├── __init__.py
│   │   │   │   ├── advanced_chat
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── app_config_manager.py
│   │   │   │   │   ├── app_generator.py
│   │   │   │   │   ├── app_runner.py
│   │   │   │   │   ├── generate_response_converter.py
│   │   │   │   │   ├── generate_task_pipeline.py
│   │   │   │   │   └── workflow_event_trigger_callback.py
│   │   │   │   ├── agent_chat
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── app_config_manager.py
│   │   │   │   │   ├── app_generator.py
│   │   │   │   │   ├── app_runner.py
│   │   │   │   │   └── generate_response_converter.py
│   │   │   │   ├── base_app_generate_response_converter.py
│   │   │   │   ├── base_app_generator.py
│   │   │   │   ├── base_app_queue_manager.py
│   │   │   │   ├── base_app_runner.py
│   │   │   │   ├── chat
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── app_config_manager.py
│   │   │   │   │   ├── app_generator.py
│   │   │   │   │   ├── app_runner.py
│   │   │   │   │   └── generate_response_converter.py
│   │   │   │   ├── completion
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── app_config_manager.py
│   │   │   │   │   ├── app_generator.py
│   │   │   │   │   ├── app_runner.py
│   │   │   │   │   └── generate_response_converter.py
│   │   │   │   ├── message_based_app_generator.py
│   │   │   │   ├── message_based_app_queue_manager.py
│   │   │   │   ├── workflow
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── app_config_manager.py
│   │   │   │   │   ├── app_generator.py
│   │   │   │   │   ├── app_queue_manager.py
│   │   │   │   │   ├── app_runner.py
│   │   │   │   │   ├── generate_response_converter.py
│   │   │   │   │   ├── generate_task_pipeline.py
│   │   │   │   │   └── workflow_event_trigger_callback.py
│   │   │   │   └── workflow_logging_callback.py
│   │   │   ├── entities
│   │   │   │   ├── __init__.py
│   │   │   │   ├── app_invoke_entities.py
│   │   │   │   ├── queue_entities.py
│   │   │   │   └── task_entities.py
│   │   │   ├── features
│   │   │   │   ├── __init__.py
│   │   │   │   ├── annotation_reply
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   └── annotation_reply.py
│   │   │   │   └── hosting_moderation
│   │   │   │       ├── __init__.py
│   │   │   │       └── hosting_moderation.py
│   │   │   └── task_pipeline
│   │   │       ├── __init__.py
│   │   │       ├── based_generate_task_pipeline.py
│   │   │       ├── easy_ui_based_generate_task_pipeline.py
│   │   │       ├── message_cycle_manage.py
│   │   │       └── workflow_cycle_manage.py
│   │   ├── application_manager.py
│   │   ├── callback_handler
│   │   │   ├── __init__.py
│   │   │   ├── agent_tool_callback_handler.py
│   │   │   ├── index_tool_callback_handler.py
│   │   │   └── workflow_tool_callback_handler.py
│   │   ├── docstore
│   │   │   └── dataset_docstore.py
│   │   ├── embedding
│   │   │   └── cached_embedding.py
│   │   ├── entities
│   │   │   ├── __init__.py
│   │   │   ├── agent_entities.py
│   │   │   ├── message_entities.py
│   │   │   ├── model_entities.py
│   │   │   ├── provider_configuration.py
│   │   │   └── provider_entities.py
│   │   ├── errors
│   │   │   ├── __init__.py
│   │   │   └── error.py
│   │   ├── extension
│   │   │   ├── __init__.py
│   │   │   ├── api_based_extension_requestor.py
│   │   │   ├── extensible.py
│   │   │   └── extension.py
│   │   ├── external_data_tool
│   │   │   ├── __init__.py
│   │   │   ├── api
│   │   │   │   ├── __builtin__
│   │   │   │   ├── __init__.py
│   │   │   │   └── api.py
│   │   │   ├── base.py
│   │   │   ├── external_data_fetch.py
│   │   │   └── factory.py
│   │   ├── file
│   │   │   ├── __init__.py
│   │   │   ├── file_obj.py
│   │   │   ├── message_file_parser.py
│   │   │   ├── tool_file_parser.py
│   │   │   └── upload_file_parser.py
│   │   ├── helper
│   │   │   ├── __init__.py
│   │   │   ├── code_executor
│   │   │   │   ├── code_executor.py
│   │   │   │   ├── entities.py
│   │   │   │   ├── javascript_transformer.py
│   │   │   │   ├── jinja2_formatter.py
│   │   │   │   ├── jinja2_transformer.py
│   │   │   │   ├── python_transformer.py
│   │   │   │   └── template_transformer.py
│   │   │   ├── encrypter.py
│   │   │   ├── lru_cache.py
│   │   │   ├── model_provider_cache.py
│   │   │   ├── moderation.py
│   │   │   ├── ssrf_proxy.py
│   │   │   ├── tool_parameter_cache.py
│   │   │   └── tool_provider_cache.py
│   │   ├── hosting_configuration.py
│   │   ├── indexing_runner.py
│   │   ├── llm_generator
│   │   │   ├── __init__.py
│   │   │   ├── llm_generator.py
│   │   │   ├── output_parser
│   │   │   │   ├── __init__.py
│   │   │   │   ├── errors.py
│   │   │   │   ├── rule_config_generator.py
│   │   │   │   └── suggested_questions_after_answer.py
│   │   │   └── prompts.py
│   │   ├── memory
│   │   │   └── token_buffer_memory.py
│   │   ├── model_manager.py
│   │   ├── model_runtime
│   │   │   ├── README.md
│   │   │   ├── README_CN.md
│   │   │   ├── __init__.py
│   │   │   ├── callbacks
│   │   │   │   ├── __init__.py
│   │   │   │   ├── base_callback.py
│   │   │   │   └── logging_callback.py
│   │   │   ├── docs
│   │   │   │   ├── en_US
│   │   │   │   │   ├── images
│   │   │   │   │   │   └── index
│   │   │   │   │   │       ├── image-20231210143654461.png
│   │   │   │   │   │       ├── image-20231210144229650.png
│   │   │   │   │   │       ├── image-20231210144814617.png
│   │   │   │   │   │       ├── image-20231210151548521.png
│   │   │   │   │   │       ├── image-20231210151628992.png
│   │   │   │   │   │       └── image-20231210165243632.png
│   │   │   │   │   ├── interfaces.md
│   │   │   │   │   ├── provider_scale_out.md
│   │   │   │   │   └── schema.md
│   │   │   │   └── zh_Hans
│   │   │   │       ├── customizable_model_scale_out.md
│   │   │   │       ├── images
│   │   │   │       │   └── index
│   │   │   │       │       ├── image-1.png
│   │   │   │       │       ├── image-2.png
│   │   │   │       │       ├── image-20231210143654461.png
│   │   │   │       │       ├── image-20231210144229650.png
│   │   │   │       │       ├── image-20231210144814617.png
│   │   │   │       │       ├── image-20231210151548521.png
│   │   │   │       │       ├── image-20231210151628992.png
│   │   │   │       │       ├── image-20231210165243632.png
│   │   │   │       │       ├── image-3.png
│   │   │   │       │       └── image.png
│   │   │   │       ├── interfaces.md
│   │   │   │       ├── predefined_model_scale_out.md
│   │   │   │       ├── provider_scale_out.md
│   │   │   │       └── schema.md
│   │   │   ├── entities
│   │   │   │   ├── __init__.py
│   │   │   │   ├── common_entities.py
│   │   │   │   ├── defaults.py
│   │   │   │   ├── llm_entities.py
│   │   │   │   ├── message_entities.py
│   │   │   │   ├── model_entities.py
│   │   │   │   ├── provider_entities.py
│   │   │   │   ├── rerank_entities.py
│   │   │   │   └── text_embedding_entities.py
│   │   │   ├── errors
│   │   │   │   ├── __init__.py
│   │   │   │   ├── invoke.py
│   │   │   │   └── validate.py
│   │   │   ├── model_providers
│   │   │   │   ├── __base
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── ai_model.py
│   │   │   │   │   ├── audio.mp3
│   │   │   │   │   ├── large_language_model.py
│   │   │   │   │   ├── model_provider.py
│   │   │   │   │   ├── moderation_model.py
│   │   │   │   │   ├── rerank_model.py
│   │   │   │   │   ├── speech2text_model.py
│   │   │   │   │   ├── text2img_model.py
│   │   │   │   │   ├── text_embedding_model.py
│   │   │   │   │   ├── tokenizers
│   │   │   │   │   │   ├── gpt2
│   │   │   │   │   │   │   ├── merges.txt
│   │   │   │   │   │   │   ├── special_tokens_map.json
│   │   │   │   │   │   │   ├── tokenizer_config.json
│   │   │   │   │   │   │   └── vocab.json
│   │   │   │   │   │   └── gpt2_tokenzier.py
│   │   │   │   │   └── tts_model.py
│   │   │   │   ├── __init__.py
│   │   │   │   ├── _position.yaml
│   │   │   │   ├── anthropic
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── _assets
│   │   │   │   │   │   ├── icon_l_en.svg
│   │   │   │   │   │   └── icon_s_en.svg
│   │   │   │   │   ├── anthropic.py
│   │   │   │   │   ├── anthropic.yaml
│   │   │   │   │   └── llm
│   │   │   │   │       ├── __init__.py
│   │   │   │   │       ├── _position.yaml
│   │   │   │   │       ├── claude-2.1.yaml
│   │   │   │   │       ├── claude-2.yaml
│   │   │   │   │       ├── claude-3-haiku-20240307.yaml
│   │   │   │   │       ├── claude-3-opus-20240229.yaml
│   │   │   │   │       ├── claude-3-sonnet-20240229.yaml
│   │   │   │   │       ├── claude-instant-1.2.yaml
│   │   │   │   │       ├── claude-instant-1.yaml
│   │   │   │   │       └── llm.py
│   │   │   │   ├── azure_openai
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── _assets
│   │   │   │   │   │   ├── icon_l_en.png
│   │   │   │   │   │   └── icon_s_en.svg
│   │   │   │   │   ├── _common.py
│   │   │   │   │   ├── _constant.py
│   │   │   │   │   ├── azure_openai.py
│   │   │   │   │   ├── azure_openai.yaml
│   │   │   │   │   ├── llm
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   └── llm.py
│   │   │   │   │   ├── speech2text
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   └── speech2text.py
│   │   │   │   │   ├── text_embedding
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   └── text_embedding.py
│   │   │   │   │   └── tts
│   │   │   │   │       ├── __init__.py
│   │   │   │   │       └── tts.py
│   │   │   │   ├── baichuan
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── _assets
│   │   │   │   │   │   ├── icon_l_en.svg
│   │   │   │   │   │   └── icon_s_en.svg
│   │   │   │   │   ├── baichuan.py
│   │   │   │   │   ├── baichuan.yaml
│   │   │   │   │   ├── llm
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── baichuan2-53b.yaml
│   │   │   │   │   │   ├── baichuan2-turbo-192k.yaml
│   │   │   │   │   │   ├── baichuan2-turbo.yaml
│   │   │   │   │   │   ├── baichuan_tokenizer.py
│   │   │   │   │   │   ├── baichuan_turbo.py
│   │   │   │   │   │   ├── baichuan_turbo_errors.py
│   │   │   │   │   │   └── llm.py
│   │   │   │   │   └── text_embedding
│   │   │   │   │       ├── __init__.py
│   │   │   │   │       ├── baichuan-text-embedding.yaml
│   │   │   │   │       └── text_embedding.py
│   │   │   │   ├── bedrock
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── _assets
│   │   │   │   │   │   ├── icon_l_en.svg
│   │   │   │   │   │   └── icon_s_en.svg
│   │   │   │   │   ├── bedrock.py
│   │   │   │   │   ├── bedrock.yaml
│   │   │   │   │   ├── llm
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── _position.yaml
│   │   │   │   │   │   ├── ai21.j2-mid-v1.yaml
│   │   │   │   │   │   ├── ai21.j2-ultra-v1.yaml
│   │   │   │   │   │   ├── amazon.titan-text-express-v1.yaml
│   │   │   │   │   │   ├── amazon.titan-text-lite-v1.yaml
│   │   │   │   │   │   ├── anthropic.claude-3-haiku-v1.yaml
│   │   │   │   │   │   ├── anthropic.claude-3-opus-v1.yaml
│   │   │   │   │   │   ├── anthropic.claude-3-sonnet-v1.yaml
│   │   │   │   │   │   ├── anthropic.claude-instant-v1.yaml
│   │   │   │   │   │   ├── anthropic.claude-v1.yaml
│   │   │   │   │   │   ├── anthropic.claude-v2.1.yaml
│   │   │   │   │   │   ├── anthropic.claude-v2.yaml
│   │   │   │   │   │   ├── cohere.command-light-text-v14.yaml
│   │   │   │   │   │   ├── cohere.command-text-v14.yaml
│   │   │   │   │   │   ├── llm.py
│   │   │   │   │   │   ├── meta.llama2-13b-chat-v1.yaml
│   │   │   │   │   │   ├── meta.llama2-70b-chat-v1.yaml
│   │   │   │   │   │   ├── meta.llama3-70b-instruct-v1.yaml
│   │   │   │   │   │   ├── meta.llama3-8b-instruct-v1.yaml
│   │   │   │   │   │   ├── mistral.mistral-7b-instruct-v0.2.yaml
│   │   │   │   │   │   ├── mistral.mistral-large-2402-v1.0.yaml
│   │   │   │   │   │   └── mistral.mixtral-8x7b-instruct-v0.1.yaml
│   │   │   │   │   └── text_embedding
│   │   │   │   │       ├── __init__.py
│   │   │   │   │       ├── _position.yaml
│   │   │   │   │       ├── amazon.titan-embed-text-v1.yaml
│   │   │   │   │       ├── cohere.embed-english-v3.yaml
│   │   │   │   │       ├── cohere.embed-multilingual-v3.yaml
│   │   │   │   │       └── text_embedding.py
│   │   │   │   ├── chatglm
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── _assets
│   │   │   │   │   │   ├── icon_l_en.svg
│   │   │   │   │   │   └── icon_s_en.svg
│   │   │   │   │   ├── chatglm.py
│   │   │   │   │   ├── chatglm.yaml
│   │   │   │   │   └── llm
│   │   │   │   │       ├── __init__.py
│   │   │   │   │       ├── chatglm2-6b-32k.yaml
│   │   │   │   │       ├── chatglm2-6b.yaml
│   │   │   │   │       ├── chatglm3-6b-32k.yaml
│   │   │   │   │       ├── chatglm3-6b.yaml
│   │   │   │   │       └── llm.py
│   │   │   │   ├── cohere
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── _assets
│   │   │   │   │   │   ├── icon_l_en.svg
│   │   │   │   │   │   └── icon_s_en.svg
│   │   │   │   │   ├── cohere.py
│   │   │   │   │   ├── cohere.yaml
│   │   │   │   │   ├── llm
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── _position.yaml
│   │   │   │   │   │   ├── command-chat.yaml
│   │   │   │   │   │   ├── command-light-chat.yaml
│   │   │   │   │   │   ├── command-light-nightly-chat.yaml
│   │   │   │   │   │   ├── command-light-nightly.yaml
│   │   │   │   │   │   ├── command-light.yaml
│   │   │   │   │   │   ├── command-nightly-chat.yaml
│   │   │   │   │   │   ├── command-nightly.yaml
│   │   │   │   │   │   ├── command-r-plus.yaml
│   │   │   │   │   │   ├── command-r.yaml
│   │   │   │   │   │   ├── command.yaml
│   │   │   │   │   │   └── llm.py
│   │   │   │   │   ├── rerank
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── _position.yaml
│   │   │   │   │   │   ├── rerank-english-v2.0.yaml
│   │   │   │   │   │   ├── rerank-english-v3.0.yaml
│   │   │   │   │   │   ├── rerank-multilingual-v2.0.yaml
│   │   │   │   │   │   ├── rerank-multilingual-v3.0.yaml
│   │   │   │   │   │   └── rerank.py
│   │   │   │   │   └── text_embedding
│   │   │   │   │       ├── __init__.py
│   │   │   │   │       ├── _position.yaml
│   │   │   │   │       ├── embed-english-light-v2.0.yaml
│   │   │   │   │       ├── embed-english-light-v3.0.yaml
│   │   │   │   │       ├── embed-english-v2.0.yaml
│   │   │   │   │       ├── embed-english-v3.0.yaml
│   │   │   │   │       ├── embed-multilingual-light-v3.0.yaml
│   │   │   │   │       ├── embed-multilingual-v2.0.yaml
│   │   │   │   │       ├── embed-multilingual-v3.0.yaml
│   │   │   │   │       └── text_embedding.py
│   │   │   │   ├── deepseek
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── _assets
│   │   │   │   │   │   ├── icon_l_en.svg
│   │   │   │   │   │   └── icon_s_en.svg
│   │   │   │   │   ├── deepseek.py
│   │   │   │   │   ├── deepseek.yaml
│   │   │   │   │   └── llm
│   │   │   │   │       ├── __init__.py
│   │   │   │   │       ├── _position.yaml
│   │   │   │   │       ├── deepseek-chat.yaml
│   │   │   │   │       ├── deepseek-coder.yaml
│   │   │   │   │       └── llm.py
│   │   │   │   ├── google
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── _assets
│   │   │   │   │   │   ├── icon_l_en.svg
│   │   │   │   │   │   └── icon_s_en.svg
│   │   │   │   │   ├── google.py
│   │   │   │   │   ├── google.yaml
│   │   │   │   │   └── llm
│   │   │   │   │       ├── __init__.py
│   │   │   │   │       ├── gemini-1.5-pro-latest.yaml
│   │   │   │   │       ├── gemini-pro-vision.yaml
│   │   │   │   │       ├── gemini-pro.yaml
│   │   │   │   │       └── llm.py
│   │   │   │   ├── groq
│   │   │   │   │   ├── _assets
│   │   │   │   │   │   ├── icon_l_en.svg
│   │   │   │   │   │   └── icon_s_en.svg
│   │   │   │   │   ├── groq.py
│   │   │   │   │   ├── groq.yaml
│   │   │   │   │   └── llm
│   │   │   │   │       ├── llama2-70b-4096.yaml
│   │   │   │   │       ├── llama3-70b-8192.yaml
│   │   │   │   │       ├── llama3-8b-8192.yaml
│   │   │   │   │       ├── llm.py
│   │   │   │   │       └── mixtral-8x7b-instruct-v0.1.yaml
│   │   │   │   ├── huggingface_hub
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── _assets
│   │   │   │   │   │   ├── icon_l_en.svg
│   │   │   │   │   │   └── icon_s_en.svg
│   │   │   │   │   ├── _common.py
│   │   │   │   │   ├── huggingface_hub.py
│   │   │   │   │   ├── huggingface_hub.yaml
│   │   │   │   │   ├── llm
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   └── llm.py
│   │   │   │   │   └── text_embedding
│   │   │   │   │       ├── __init__.py
│   │   │   │   │       └── text_embedding.py
│   │   │   │   ├── jina
│   │   │   │   │   ├── _assets
│   │   │   │   │   │   ├── icon_l_en.svg
│   │   │   │   │   │   └── icon_s_en.svg
│   │   │   │   │   ├── jina.py
│   │   │   │   │   ├── jina.yaml
│   │   │   │   │   ├── rerank
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── jina-colbert-v1-en.yaml
│   │   │   │   │   │   ├── jina-reranker-v1-base-en.yaml
│   │   │   │   │   │   └── rerank.py
│   │   │   │   │   └── text_embedding
│   │   │   │   │       ├── jina-embeddings-v2-base-de.yaml
│   │   │   │   │       ├── jina-embeddings-v2-base-en.yaml
│   │   │   │   │       ├── jina-embeddings-v2-base-zh.yaml
│   │   │   │   │       ├── jina-embeddings-v2-small-en.yaml
│   │   │   │   │       ├── jina_tokenizer.py
│   │   │   │   │       ├── text_embedding.py
│   │   │   │   │       └── tokenizer
│   │   │   │   │           ├── tokenizer.json
│   │   │   │   │           └── tokenizer_config.json
│   │   │   │   ├── leptonai
│   │   │   │   │   ├── _assets
│   │   │   │   │   │   ├── icon_l_en.png
│   │   │   │   │   │   └── icon_s_en.png
│   │   │   │   │   ├── leptonai.py
│   │   │   │   │   ├── leptonai.yaml
│   │   │   │   │   └── llm
│   │   │   │   │       ├── _position.yaml
│   │   │   │   │       ├── gemma-7b.yaml
│   │   │   │   │       ├── llama2-13b.yaml
│   │   │   │   │       ├── llama2-7b.yaml
│   │   │   │   │       ├── llama3-70b.yaml
│   │   │   │   │       ├── llm.py
│   │   │   │   │       ├── mistral-7b.yaml
│   │   │   │   │       └── mixtral-8x7b.yaml
│   │   │   │   ├── localai
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── _assets
│   │   │   │   │   │   ├── icon_l_en.svg
│   │   │   │   │   │   └── icon_s_en.svg
│   │   │   │   │   ├── llm
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   └── llm.py
│   │   │   │   │   ├── localai.py
│   │   │   │   │   ├── localai.yaml
│   │   │   │   │   ├── rerank
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   └── rerank.py
│   │   │   │   │   ├── speech2text
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   └── speech2text.py
│   │   │   │   │   └── text_embedding
│   │   │   │   │       ├── __init__.py
│   │   │   │   │       └── text_embedding.py
│   │   │   │   ├── minimax
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── _assets
│   │   │   │   │   │   ├── icon_l_en.png
│   │   │   │   │   │   └── icon_s_en.png
│   │   │   │   │   ├── llm
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── abab5-chat.yaml
│   │   │   │   │   │   ├── abab5.5-chat.yaml
│   │   │   │   │   │   ├── abab5.5s-chat.yaml
│   │   │   │   │   │   ├── abab6-chat.yaml
│   │   │   │   │   │   ├── abab6.5-chat.yaml
│   │   │   │   │   │   ├── abab6.5s-chat.yaml
│   │   │   │   │   │   ├── chat_completion.py
│   │   │   │   │   │   ├── chat_completion_pro.py
│   │   │   │   │   │   ├── errors.py
│   │   │   │   │   │   ├── llm.py
│   │   │   │   │   │   └── types.py
│   │   │   │   │   ├── minimax.py
│   │   │   │   │   ├── minimax.yaml
│   │   │   │   │   └── text_embedding
│   │   │   │   │       ├── __init__.py
│   │   │   │   │       ├── embo-01.yaml
│   │   │   │   │       └── text_embedding.py
│   │   │   │   ├── mistralai
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── _assets
│   │   │   │   │   │   ├── icon_l_en.png
│   │   │   │   │   │   └── icon_s_en.png
│   │   │   │   │   ├── llm
│   │   │   │   │   │   ├── _position.yaml
│   │   │   │   │   │   ├── llm.py
│   │   │   │   │   │   ├── mistral-large-latest.yaml
│   │   │   │   │   │   ├── mistral-medium-latest.yaml
│   │   │   │   │   │   ├── mistral-small-latest.yaml
│   │   │   │   │   │   ├── open-mistral-7b.yaml
│   │   │   │   │   │   ├── open-mixtral-8x22b.yaml
│   │   │   │   │   │   └── open-mixtral-8x7b.yaml
│   │   │   │   │   ├── mistralai.py
│   │   │   │   │   └── mistralai.yaml
│   │   │   │   ├── model_provider_factory.py
│   │   │   │   ├── moonshot
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── _assets
│   │   │   │   │   │   ├── icon_l_en.png
│   │   │   │   │   │   └── icon_s_en.png
│   │   │   │   │   ├── llm
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── _position.yaml
│   │   │   │   │   │   ├── llm.py
│   │   │   │   │   │   ├── moonshot-v1-128k.yaml
│   │   │   │   │   │   ├── moonshot-v1-32k.yaml
│   │   │   │   │   │   └── moonshot-v1-8k.yaml
│   │   │   │   │   ├── moonshot.py
│   │   │   │   │   └── moonshot.yaml
│   │   │   │   ├── nvidia
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── _assets
│   │   │   │   │   │   ├── icon_l_en.png
│   │   │   │   │   │   └── icon_s_en.svg
│   │   │   │   │   ├── llm
│   │   │   │   │   │   ├── _position.yaml
│   │   │   │   │   │   ├── arctic.yaml
│   │   │   │   │   │   ├── codegemma-7b.yaml
│   │   │   │   │   │   ├── fuyu-8b.yaml
│   │   │   │   │   │   ├── gemma-7b.yaml
│   │   │   │   │   │   ├── llama2-70b.yaml
│   │   │   │   │   │   ├── llama3-70b.yaml
│   │   │   │   │   │   ├── llama3-8b.yaml
│   │   │   │   │   │   ├── llm.py
│   │   │   │   │   │   ├── mistral-large.yaml
│   │   │   │   │   │   ├── mistralai_mixtral-8x7b-instruct-v0.1.yaml
│   │   │   │   │   │   ├── mixtral-8x22b-instruct-v0.1.yaml
│   │   │   │   │   │   └── recurrentgemma-2b.yaml
│   │   │   │   │   ├── nvidia.py
│   │   │   │   │   ├── nvidia.yaml
│   │   │   │   │   ├── rerank
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── rerank-qa-mistral-4b.yaml
│   │   │   │   │   │   └── rerank.py
│   │   │   │   │   └── text_embedding
│   │   │   │   │       ├── __init__.py
│   │   │   │   │       ├── embed-qa-4.yaml
│   │   │   │   │       └── text_embedding.py
│   │   │   │   ├── ollama
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── _assets
│   │   │   │   │   │   ├── icon_l_en.svg
│   │   │   │   │   │   └── icon_s_en.svg
│   │   │   │   │   ├── llm
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   └── llm.py
│   │   │   │   │   ├── ollama.py
│   │   │   │   │   ├── ollama.yaml
│   │   │   │   │   └── text_embedding
│   │   │   │   │       ├── __init__.py
│   │   │   │   │       └── text_embedding.py
│   │   │   │   ├── openai
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── _assets
│   │   │   │   │   │   ├── icon_l_en.svg
│   │   │   │   │   │   └── icon_s_en.svg
│   │   │   │   │   ├── _common.py
│   │   │   │   │   ├── llm
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── _position.yaml
│   │   │   │   │   │   ├── gpt-3.5-turbo-0125.yaml
│   │   │   │   │   │   ├── gpt-3.5-turbo-0613.yaml
│   │   │   │   │   │   ├── gpt-3.5-turbo-1106.yaml
│   │   │   │   │   │   ├── gpt-3.5-turbo-16k-0613.yaml
│   │   │   │   │   │   ├── gpt-3.5-turbo-16k.yaml
│   │   │   │   │   │   ├── gpt-3.5-turbo-instruct.yaml
│   │   │   │   │   │   ├── gpt-3.5-turbo.yaml
│   │   │   │   │   │   ├── gpt-4-0125-preview.yaml
│   │   │   │   │   │   ├── gpt-4-1106-preview.yaml
│   │   │   │   │   │   ├── gpt-4-32k.yaml
│   │   │   │   │   │   ├── gpt-4-turbo-2024-04-09.yaml
│   │   │   │   │   │   ├── gpt-4-turbo-preview.yaml
│   │   │   │   │   │   ├── gpt-4-turbo.yaml
│   │   │   │   │   │   ├── gpt-4-vision-preview.yaml
│   │   │   │   │   │   ├── gpt-4.yaml
│   │   │   │   │   │   ├── gpt-4o-2024-05-13.yaml
│   │   │   │   │   │   ├── gpt-4o.yaml
│   │   │   │   │   │   ├── llm.py
│   │   │   │   │   │   └── text-davinci-003.yaml
│   │   │   │   │   ├── moderation
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── moderation.py
│   │   │   │   │   │   └── text-moderation-stable.yaml
│   │   │   │   │   ├── openai.py
│   │   │   │   │   ├── openai.yaml
│   │   │   │   │   ├── speech2text
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── speech2text.py
│   │   │   │   │   │   └── whisper-1.yaml
│   │   │   │   │   ├── text_embedding
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── text-embedding-3-large.yaml
│   │   │   │   │   │   ├── text-embedding-3-small.yaml
│   │   │   │   │   │   ├── text-embedding-ada-002.yaml
│   │   │   │   │   │   └── text_embedding.py
│   │   │   │   │   └── tts
│   │   │   │   │       ├── __init__.py
│   │   │   │   │       ├── tts-1-hd.yaml
│   │   │   │   │       ├── tts-1.yaml
│   │   │   │   │       └── tts.py
│   │   │   │   ├── openai_api_compatible
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── _common.py
│   │   │   │   │   ├── llm
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   └── llm.py
│   │   │   │   │   ├── openai_api_compatible.py
│   │   │   │   │   ├── openai_api_compatible.yaml
│   │   │   │   │   └── text_embedding
│   │   │   │   │       ├── __init__.py
│   │   │   │   │       └── text_embedding.py
│   │   │   │   ├── openllm
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── _assets
│   │   │   │   │   │   ├── icon_l_en.svg
│   │   │   │   │   │   └── icon_s_en.svg
│   │   │   │   │   ├── llm
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── llm.py
│   │   │   │   │   │   ├── openllm_generate.py
│   │   │   │   │   │   └── openllm_generate_errors.py
│   │   │   │   │   ├── openllm.py
│   │   │   │   │   ├── openllm.yaml
│   │   │   │   │   └── text_embedding
│   │   │   │   │       ├── __init__.py
│   │   │   │   │       └── text_embedding.py
│   │   │   │   ├── openrouter
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── _assets
│   │   │   │   │   │   ├── openrouter.svg
│   │   │   │   │   │   └── openrouter_square.svg
│   │   │   │   │   ├── llm
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   └── llm.py
│   │   │   │   │   ├── openrouter.py
│   │   │   │   │   └── openrouter.yaml
│   │   │   │   ├── replicate
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── _assets
│   │   │   │   │   │   ├── icon_l_en.svg
│   │   │   │   │   │   └── icon_s_en.svg
│   │   │   │   │   ├── _common.py
│   │   │   │   │   ├── llm
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   └── llm.py
│   │   │   │   │   ├── replicate.py
│   │   │   │   │   ├── replicate.yaml
│   │   │   │   │   └── text_embedding
│   │   │   │   │       ├── __init__.py
│   │   │   │   │       └── text_embedding.py
│   │   │   │   ├── spark
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── _assets
│   │   │   │   │   │   ├── icon_l_en.svg
│   │   │   │   │   │   ├── icon_l_zh.svg
│   │   │   │   │   │   └── icon_s_en.svg
│   │   │   │   │   ├── llm
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── _client.py
│   │   │   │   │   │   ├── _position.yaml
│   │   │   │   │   │   ├── llm.py
│   │   │   │   │   │   ├── spark-1.5.yaml
│   │   │   │   │   │   ├── spark-2.yaml
│   │   │   │   │   │   ├── spark-3.5.yaml
│   │   │   │   │   │   └── spark-3.yaml
│   │   │   │   │   ├── spark.py
│   │   │   │   │   └── spark.yaml
│   │   │   │   ├── togetherai
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── _assets
│   │   │   │   │   │   ├── togetherai.svg
│   │   │   │   │   │   └── togetherai_square.svg
│   │   │   │   │   ├── llm
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   └── llm.py
│   │   │   │   │   ├── togetherai.py
│   │   │   │   │   └── togetherai.yaml
│   │   │   │   ├── tongyi
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── _assets
│   │   │   │   │   │   ├── icon_l_en.png
│   │   │   │   │   │   ├── icon_l_zh.png
│   │   │   │   │   │   └── icon_s_en.png
│   │   │   │   │   ├── _common.py
│   │   │   │   │   ├── llm
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── llm.py
│   │   │   │   │   │   ├── qwen-max-0403.yaml
│   │   │   │   │   │   ├── qwen-max-1201.yaml
│   │   │   │   │   │   ├── qwen-max-longcontext.yaml
│   │   │   │   │   │   ├── qwen-max.yaml
│   │   │   │   │   │   ├── qwen-plus-chat.yaml
│   │   │   │   │   │   ├── qwen-plus.yaml
│   │   │   │   │   │   ├── qwen-turbo-chat.yaml
│   │   │   │   │   │   ├── qwen-turbo.yaml
│   │   │   │   │   │   ├── qwen-vl-max.yaml
│   │   │   │   │   │   └── qwen-vl-plus.yaml
│   │   │   │   │   ├── text_embedding
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── text-embedding-v1.yaml
│   │   │   │   │   │   ├── text-embedding-v2.yaml
│   │   │   │   │   │   └── text_embedding.py
│   │   │   │   │   ├── tongyi.py
│   │   │   │   │   ├── tongyi.yaml
│   │   │   │   │   └── tts
│   │   │   │   │       ├── __init__.py
│   │   │   │   │       ├── tts-1.yaml
│   │   │   │   │       └── tts.py
│   │   │   │   ├── triton_inference_server
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── _assets
│   │   │   │   │   │   ├── icon_l_en.png
│   │   │   │   │   │   └── icon_s_en.svg
│   │   │   │   │   ├── llm
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   └── llm.py
│   │   │   │   │   ├── triton_inference_server.py
│   │   │   │   │   └── triton_inference_server.yaml
│   │   │   │   ├── volcengine_maas
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── _assets
│   │   │   │   │   │   ├── icon_l_en.svg
│   │   │   │   │   │   ├── icon_l_zh.svg
│   │   │   │   │   │   └── icon_s_en.svg
│   │   │   │   │   ├── client.py
│   │   │   │   │   ├── errors.py
│   │   │   │   │   ├── llm
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── llm.py
│   │   │   │   │   │   └── models.py
│   │   │   │   │   ├── text_embedding
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   └── text_embedding.py
│   │   │   │   │   ├── volc_sdk
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── base
│   │   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   │   ├── auth.py
│   │   │   │   │   │   │   ├── service.py
│   │   │   │   │   │   │   └── util.py
│   │   │   │   │   │   ├── common.py
│   │   │   │   │   │   └── maas.py
│   │   │   │   │   ├── volcengine_maas.py
│   │   │   │   │   └── volcengine_maas.yaml
│   │   │   │   ├── wenxin
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── _assets
│   │   │   │   │   │   ├── icon_l_en.png
│   │   │   │   │   │   ├── icon_l_zh.png
│   │   │   │   │   │   └── icon_s_en.png
│   │   │   │   │   ├── llm
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── ernie-3.5-4k-0205.yaml
│   │   │   │   │   │   ├── ernie-3.5-8k-0205.yaml
│   │   │   │   │   │   ├── ernie-3.5-8k-1222.yaml
│   │   │   │   │   │   ├── ernie-3.5-8k.yaml
│   │   │   │   │   │   ├── ernie-4.0-8k.yaml
│   │   │   │   │   │   ├── ernie-bot-4.yaml
│   │   │   │   │   │   ├── ernie-bot-8k.yaml
│   │   │   │   │   │   ├── ernie-bot-turbo.yaml
│   │   │   │   │   │   ├── ernie-bot.yaml
│   │   │   │   │   │   ├── ernie-lite-8k-0308.yaml
│   │   │   │   │   │   ├── ernie-lite-8k-0922.yaml
│   │   │   │   │   │   ├── ernie-speed-128k.yaml
│   │   │   │   │   │   ├── ernie-speed-8k.yaml
│   │   │   │   │   │   ├── ernie-speed-appbuilder.yaml
│   │   │   │   │   │   ├── ernie_bot.py
│   │   │   │   │   │   ├── ernie_bot_errors.py
│   │   │   │   │   │   └── llm.py
│   │   │   │   │   ├── wenxin.py
│   │   │   │   │   └── wenxin.yaml
│   │   │   │   ├── xinference
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── _assets
│   │   │   │   │   │   ├── icon_l_en.svg
│   │   │   │   │   │   └── icon_s_en.svg
│   │   │   │   │   ├── llm
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   └── llm.py
│   │   │   │   │   ├── rerank
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   └── rerank.py
│   │   │   │   │   ├── speech2text
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   └── speech2text.py
│   │   │   │   │   ├── text_embedding
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   └── text_embedding.py
│   │   │   │   │   ├── xinference.py
│   │   │   │   │   ├── xinference.yaml
│   │   │   │   │   └── xinference_helper.py
│   │   │   │   ├── yi
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── _assets
│   │   │   │   │   │   ├── icon_l_en.svg
│   │   │   │   │   │   └── icon_s_en.svg
│   │   │   │   │   ├── llm
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── _position.yaml
│   │   │   │   │   │   ├── llm.py
│   │   │   │   │   │   ├── yi-34b-chat-0205.yaml
│   │   │   │   │   │   ├── yi-34b-chat-200k.yaml
│   │   │   │   │   │   ├── yi-large-turbo.yaml
│   │   │   │   │   │   ├── yi-large.yaml
│   │   │   │   │   │   ├── yi-medium-200k.yaml
│   │   │   │   │   │   ├── yi-medium.yaml
│   │   │   │   │   │   ├── yi-spark.yaml
│   │   │   │   │   │   ├── yi-vision.yaml
│   │   │   │   │   │   └── yi-vl-plus.yaml
│   │   │   │   │   ├── yi.py
│   │   │   │   │   └── yi.yaml
│   │   │   │   └── zhipuai
│   │   │   │       ├── __init__.py
│   │   │   │       ├── _assets
│   │   │   │       │   ├── icon_l_en.svg
│   │   │   │       │   ├── icon_l_zh.svg
│   │   │   │       │   └── icon_s_en.svg
│   │   │   │       ├── _common.py
│   │   │   │       ├── llm
│   │   │   │       │   ├── __init__.py
│   │   │   │       │   ├── chatglm_lite.yaml
│   │   │   │       │   ├── chatglm_lite_32k.yaml
│   │   │   │       │   ├── chatglm_pro.yaml
│   │   │   │       │   ├── chatglm_std.yaml
│   │   │   │       │   ├── chatglm_turbo.yaml
│   │   │   │       │   ├── glm_3_turbo.yaml
│   │   │   │       │   ├── glm_4.yaml
│   │   │   │       │   ├── glm_4v.yaml
│   │   │   │       │   └── llm.py
│   │   │   │       ├── text_embedding
│   │   │   │       │   ├── __init__.py
│   │   │   │       │   ├── text_embedding.py
│   │   │   │       │   └── text_embedding.yaml
│   │   │   │       ├── zhipuai.py
│   │   │   │       ├── zhipuai.yaml
│   │   │   │       └── zhipuai_sdk
│   │   │   │           ├── __init__.py
│   │   │   │           ├── __version__.py
│   │   │   │           ├── _client.py
│   │   │   │           ├── api_resource
│   │   │   │           │   ├── __init__.py
│   │   │   │           │   ├── chat
│   │   │   │           │   │   ├── __init__.py
│   │   │   │           │   │   ├── async_completions.py
│   │   │   │           │   │   ├── chat.py
│   │   │   │           │   │   └── completions.py
│   │   │   │           │   ├── embeddings.py
│   │   │   │           │   ├── files.py
│   │   │   │           │   ├── fine_tuning
│   │   │   │           │   │   ├── __init__.py
│   │   │   │           │   │   ├── fine_tuning.py
│   │   │   │           │   │   └── jobs.py
│   │   │   │           │   └── images.py
│   │   │   │           ├── core
│   │   │   │           │   ├── __init__.py
│   │   │   │           │   ├── _base_api.py
│   │   │   │           │   ├── _base_type.py
│   │   │   │           │   ├── _errors.py
│   │   │   │           │   ├── _files.py
│   │   │   │           │   ├── _http_client.py
│   │   │   │           │   ├── _jwt_token.py
│   │   │   │           │   ├── _request_opt.py
│   │   │   │           │   ├── _response.py
│   │   │   │           │   ├── _sse_client.py
│   │   │   │           │   └── _utils.py
│   │   │   │           └── types
│   │   │   │               ├── __init__.py
│   │   │   │               ├── chat
│   │   │   │               │   ├── __init__.py
│   │   │   │               │   ├── async_chat_completion.py
│   │   │   │               │   ├── chat_completion.py
│   │   │   │               │   ├── chat_completion_chunk.py
│   │   │   │               │   └── chat_completions_create_param.py
│   │   │   │               ├── embeddings.py
│   │   │   │               ├── file_object.py
│   │   │   │               ├── fine_tuning
│   │   │   │               │   ├── __init__.py
│   │   │   │               │   ├── fine_tuning_job.py
│   │   │   │               │   ├── fine_tuning_job_event.py
│   │   │   │               │   └── job_create_params.py
│   │   │   │               └── image.py
│   │   │   ├── schema_validators
│   │   │   │   ├── __init__.py
│   │   │   │   ├── common_validator.py
│   │   │   │   ├── model_credential_schema_validator.py
│   │   │   │   └── provider_credential_schema_validator.py
│   │   │   └── utils
│   │   │       ├── __init__.py
│   │   │       ├── _compat.py
│   │   │       ├── encoders.py
│   │   │       └── helper.py
│   │   ├── moderation
│   │   │   ├── __init__.py
│   │   │   ├── api
│   │   │   │   ├── __builtin__
│   │   │   │   ├── __init__.py
│   │   │   │   └── api.py
│   │   │   ├── base.py
│   │   │   ├── factory.py
│   │   │   ├── input_moderation.py
│   │   │   ├── keywords
│   │   │   │   ├── __builtin__
│   │   │   │   ├── __init__.py
│   │   │   │   └── keywords.py
│   │   │   ├── openai_moderation
│   │   │   │   ├── __builtin__
│   │   │   │   ├── __init__.py
│   │   │   │   └── openai_moderation.py
│   │   │   └── output_moderation.py
│   │   ├── prompt
│   │   │   ├── __init__.py
│   │   │   ├── advanced_prompt_transform.py
│   │   │   ├── entities
│   │   │   │   ├── __init__.py
│   │   │   │   └── advanced_prompt_entities.py
│   │   │   ├── prompt_templates
│   │   │   │   ├── __init__.py
│   │   │   │   ├── advanced_prompt_templates.py
│   │   │   │   ├── baichuan_chat.json
│   │   │   │   ├── baichuan_completion.json
│   │   │   │   ├── common_chat.json
│   │   │   │   └── common_completion.json
│   │   │   ├── prompt_transform.py
│   │   │   ├── simple_prompt_transform.py
│   │   │   └── utils
│   │   │       ├── __init__.py
│   │   │       ├── prompt_message_util.py
│   │   │       └── prompt_template_parser.py
│   │   ├── provider_manager.py
│   │   ├── rag
│   │   │   ├── __init__.py
│   │   │   ├── cleaner
│   │   │   │   ├── clean_processor.py
│   │   │   │   ├── cleaner_base.py
│   │   │   │   └── unstructured
│   │   │   │       ├── unstructured_extra_whitespace_cleaner.py
│   │   │   │       ├── unstructured_group_broken_paragraphs_cleaner.py
│   │   │   │       ├── unstructured_non_ascii_chars_cleaner.py
│   │   │   │       ├── unstructured_replace_unicode_quotes_cleaner.py
│   │   │   │       └── unstructured_translate_text_cleaner.py
│   │   │   ├── data_post_processor
│   │   │   │   ├── __init__.py
│   │   │   │   ├── data_post_processor.py
│   │   │   │   └── reorder.py
│   │   │   ├── datasource
│   │   │   │   ├── __init__.py
│   │   │   │   ├── entity
│   │   │   │   │   └── embedding.py
│   │   │   │   ├── keyword
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── jieba
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── jieba.py
│   │   │   │   │   │   ├── jieba_keyword_table_handler.py
│   │   │   │   │   │   └── stopwords.py
│   │   │   │   │   ├── keyword_base.py
│   │   │   │   │   └── keyword_factory.py
│   │   │   │   ├── retrieval_service.py
│   │   │   │   └── vdb
│   │   │   │       ├── __init__.py
│   │   │   │       ├── field.py
│   │   │   │       ├── milvus
│   │   │   │       │   ├── __init__.py
│   │   │   │       │   └── milvus_vector.py
│   │   │   │       ├── pgvecto_rs
│   │   │   │       │   ├── __init__.py
│   │   │   │       │   ├── collection.py
│   │   │   │       │   └── pgvecto_rs.py
│   │   │   │       ├── pgvector
│   │   │   │       │   ├── __init__.py
│   │   │   │       │   └── pgvector.py
│   │   │   │       ├── qdrant
│   │   │   │       │   ├── __init__.py
│   │   │   │       │   └── qdrant_vector.py
│   │   │   │       ├── relyt
│   │   │   │       │   ├── __init__.py
│   │   │   │       │   └── relyt_vector.py
│   │   │   │       ├── vector_base.py
│   │   │   │       ├── vector_factory.py
│   │   │   │       └── weaviate
│   │   │   │           ├── __init__.py
│   │   │   │           └── weaviate_vector.py
│   │   │   ├── extractor
│   │   │   │   ├── blod
│   │   │   │   │   └── blod.py
│   │   │   │   ├── csv_extractor.py
│   │   │   │   ├── entity
│   │   │   │   │   ├── datasource_type.py
│   │   │   │   │   └── extract_setting.py
│   │   │   │   ├── excel_extractor.py
│   │   │   │   ├── extract_processor.py
│   │   │   │   ├── extractor_base.py
│   │   │   │   ├── helpers.py
│   │   │   │   ├── html_extractor.py
│   │   │   │   ├── markdown_extractor.py
│   │   │   │   ├── notion_extractor.py
│   │   │   │   ├── pdf_extractor.py
│   │   │   │   ├── text_extractor.py
│   │   │   │   ├── unstructured
│   │   │   │   │   ├── unstructured_doc_extractor.py
│   │   │   │   │   ├── unstructured_eml_extractor.py
│   │   │   │   │   ├── unstructured_epub_extractor.py
│   │   │   │   │   ├── unstructured_markdown_extractor.py
│   │   │   │   │   ├── unstructured_msg_extractor.py
│   │   │   │   │   ├── unstructured_ppt_extractor.py
│   │   │   │   │   ├── unstructured_pptx_extractor.py
│   │   │   │   │   ├── unstructured_text_extractor.py
│   │   │   │   │   └── unstructured_xml_extractor.py
│   │   │   │   └── word_extractor.py
│   │   │   ├── index_processor
│   │   │   │   ├── __init__.py
│   │   │   │   ├── constant
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   └── index_type.py
│   │   │   │   ├── index_processor_base.py
│   │   │   │   ├── index_processor_factory.py
│   │   │   │   └── processor
│   │   │   │       ├── __init__.py
│   │   │   │       ├── paragraph_index_processor.py
│   │   │   │       └── qa_index_processor.py
│   │   │   ├── models
│   │   │   │   ├── __init__.py
│   │   │   │   └── document.py
│   │   │   └── retrieval
│   │   │       ├── __init__.py
│   │   │       ├── dataset_retrieval.py
│   │   │       ├── output_parser
│   │   │       │   ├── __init__.py
│   │   │       │   ├── react_output.py
│   │   │       │   └── structured_chat.py
│   │   │       └── router
│   │   │           ├── multi_dataset_function_call_router.py
│   │   │           └── multi_dataset_react_route.py
│   │   ├── rerank
│   │   │   ├── __init__.py
│   │   │   └── rerank.py
│   │   ├── splitter
│   │   │   ├── fixed_text_splitter.py
│   │   │   └── text_splitter.py
│   │   ├── tools
│   │   │   ├── README.md
│   │   │   ├── README_CN.md
│   │   │   ├── docs
│   │   │   │   ├── en_US
│   │   │   │   │   ├── advanced_scale_out.md
│   │   │   │   │   └── tool_scale_out.md
│   │   │   │   └── zh_Hans
│   │   │   │       ├── advanced_scale_out.md
│   │   │   │       ├── images
│   │   │   │       │   └── index
│   │   │   │       │       ├── image-1.png
│   │   │   │       │       ├── image-2.png
│   │   │   │       │       └── image.png
│   │   │   │       └── tool_scale_out.md
│   │   │   ├── entities
│   │   │   │   ├── common_entities.py
│   │   │   │   ├── constant.py
│   │   │   │   ├── tool_bundle.py
│   │   │   │   ├── tool_entities.py
│   │   │   │   └── user_entities.py
│   │   │   ├── errors.py
│   │   │   ├── model
│   │   │   │   ├── errors.py
│   │   │   │   └── tool_model_manager.py
│   │   │   ├── prompt
│   │   │   │   └── template.py
│   │   │   ├── provider
│   │   │   │   ├── _position.yaml
│   │   │   │   ├── api_tool_provider.py
│   │   │   │   ├── app_tool_provider.py
│   │   │   │   ├── builtin
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── _positions.py
│   │   │   │   │   ├── aippt
│   │   │   │   │   │   ├── _assets
│   │   │   │   │   │   │   └── icon.png
│   │   │   │   │   │   ├── aippt.py
│   │   │   │   │   │   ├── aippt.yaml
│   │   │   │   │   │   └── tools
│   │   │   │   │   │       ├── aippt.py
│   │   │   │   │   │       └── aippt.yaml
│   │   │   │   │   ├── arxiv
│   │   │   │   │   │   ├── _assets
│   │   │   │   │   │   │   └── icon.svg
│   │   │   │   │   │   ├── arxiv.py
│   │   │   │   │   │   ├── arxiv.yaml
│   │   │   │   │   │   └── tools
│   │   │   │   │   │       ├── arxiv_search.py
│   │   │   │   │   │       └── arxiv_search.yaml
│   │   │   │   │   ├── azuredalle
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── _assets
│   │   │   │   │   │   │   └── icon.png
│   │   │   │   │   │   ├── azuredalle.py
│   │   │   │   │   │   ├── azuredalle.yaml
│   │   │   │   │   │   └── tools
│   │   │   │   │   │       ├── dalle3.py
│   │   │   │   │   │       └── dalle3.yaml
│   │   │   │   │   ├── bing
│   │   │   │   │   │   ├── _assets
│   │   │   │   │   │   │   └── icon.svg
│   │   │   │   │   │   ├── bing.py
│   │   │   │   │   │   ├── bing.yaml
│   │   │   │   │   │   └── tools
│   │   │   │   │   │       ├── bing_web_search.py
│   │   │   │   │   │       └── bing_web_search.yaml
│   │   │   │   │   ├── brave
│   │   │   │   │   │   ├── _assets
│   │   │   │   │   │   │   └── icon.svg
│   │   │   │   │   │   ├── brave.py
│   │   │   │   │   │   ├── brave.yaml
│   │   │   │   │   │   └── tools
│   │   │   │   │   │       ├── brave_search.py
│   │   │   │   │   │       └── brave_search.yaml
│   │   │   │   │   ├── chart
│   │   │   │   │   │   ├── _assets
│   │   │   │   │   │   │   └── icon.png
│   │   │   │   │   │   ├── chart.py
│   │   │   │   │   │   ├── chart.yaml
│   │   │   │   │   │   └── tools
│   │   │   │   │   │       ├── bar.py
│   │   │   │   │   │       ├── bar.yaml
│   │   │   │   │   │       ├── line.py
│   │   │   │   │   │       ├── line.yaml
│   │   │   │   │   │       ├── pie.py
│   │   │   │   │   │       └── pie.yaml
│   │   │   │   │   ├── code
│   │   │   │   │   │   ├── _assets
│   │   │   │   │   │   │   └── icon.svg
│   │   │   │   │   │   ├── code.py
│   │   │   │   │   │   ├── code.yaml
│   │   │   │   │   │   └── tools
│   │   │   │   │   │       ├── simple_code.py
│   │   │   │   │   │       └── simple_code.yaml
│   │   │   │   │   ├── dalle
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── _assets
│   │   │   │   │   │   │   └── icon.png
│   │   │   │   │   │   ├── dalle.py
│   │   │   │   │   │   ├── dalle.yaml
│   │   │   │   │   │   └── tools
│   │   │   │   │   │       ├── dalle2.py
│   │   │   │   │   │       ├── dalle2.yaml
│   │   │   │   │   │       ├── dalle3.py
│   │   │   │   │   │       └── dalle3.yaml
│   │   │   │   │   ├── devdocs
│   │   │   │   │   │   ├── _assets
│   │   │   │   │   │   │   └── icon.svg
│   │   │   │   │   │   ├── devdocs.py
│   │   │   │   │   │   ├── devdocs.yaml
│   │   │   │   │   │   └── tools
│   │   │   │   │   │       ├── searchDevDocs.py
│   │   │   │   │   │       └── searchDevDocs.yaml
│   │   │   │   │   ├── dingtalk
│   │   │   │   │   │   ├── _assets
│   │   │   │   │   │   │   └── icon.svg
│   │   │   │   │   │   ├── dingtalk.py
│   │   │   │   │   │   ├── dingtalk.yaml
│   │   │   │   │   │   └── tools
│   │   │   │   │   │       ├── dingtalk_group_bot.py
│   │   │   │   │   │       └── dingtalk_group_bot.yaml
│   │   │   │   │   ├── duckduckgo
│   │   │   │   │   │   ├── _assets
│   │   │   │   │   │   │   └── icon.svg
│   │   │   │   │   │   ├── duckduckgo.py
│   │   │   │   │   │   ├── duckduckgo.yaml
│   │   │   │   │   │   └── tools
│   │   │   │   │   │       ├── duckduckgo_search.py
│   │   │   │   │   │       └── duckduckgo_search.yaml
│   │   │   │   │   ├── feishu
│   │   │   │   │   │   ├── _assets
│   │   │   │   │   │   │   └── icon.svg
│   │   │   │   │   │   ├── feishu.py
│   │   │   │   │   │   ├── feishu.yaml
│   │   │   │   │   │   └── tools
│   │   │   │   │   │       ├── feishu_group_bot.py
│   │   │   │   │   │       └── feishu_group_bot.yaml
│   │   │   │   │   ├── firecrawl
│   │   │   │   │   │   ├── _assets
│   │   │   │   │   │   │   └── icon.svg
│   │   │   │   │   │   ├── firecrawl.py
│   │   │   │   │   │   ├── firecrawl.yaml
│   │   │   │   │   │   └── tools
│   │   │   │   │   │       ├── crawl.py
│   │   │   │   │   │       └── crawl.yaml
│   │   │   │   │   ├── gaode
│   │   │   │   │   │   ├── _assets
│   │   │   │   │   │   │   └── icon.svg
│   │   │   │   │   │   ├── gaode.py
│   │   │   │   │   │   ├── gaode.yaml
│   │   │   │   │   │   └── tools
│   │   │   │   │   │       ├── gaode_weather.py
│   │   │   │   │   │       └── gaode_weather.yaml
│   │   │   │   │   ├── github
│   │   │   │   │   │   ├── _assets
│   │   │   │   │   │   │   └── icon.svg
│   │   │   │   │   │   ├── github.py
│   │   │   │   │   │   ├── github.yaml
│   │   │   │   │   │   └── tools
│   │   │   │   │   │       ├── github_repositories.py
│   │   │   │   │   │       └── github_repositories.yaml
│   │   │   │   │   ├── google
│   │   │   │   │   │   ├── _assets
│   │   │   │   │   │   │   └── icon.svg
│   │   │   │   │   │   ├── google.py
│   │   │   │   │   │   ├── google.yaml
│   │   │   │   │   │   └── tools
│   │   │   │   │   │       ├── google_search.py
│   │   │   │   │   │       └── google_search.yaml
│   │   │   │   │   ├── jina
│   │   │   │   │   │   ├── _assets
│   │   │   │   │   │   │   └── icon.svg
│   │   │   │   │   │   ├── jina.py
│   │   │   │   │   │   ├── jina.yaml
│   │   │   │   │   │   └── tools
│   │   │   │   │   │       ├── jina_reader.py
│   │   │   │   │   │       └── jina_reader.yaml
│   │   │   │   │   ├── judge0ce
│   │   │   │   │   │   ├── _assets
│   │   │   │   │   │   │   └── icon.svg
│   │   │   │   │   │   ├── judge0ce.py
│   │   │   │   │   │   ├── judge0ce.yaml
│   │   │   │   │   │   └── tools
│   │   │   │   │   │       ├── executeCode.py
│   │   │   │   │   │       └── executeCode.yaml
│   │   │   │   │   ├── maths
│   │   │   │   │   │   ├── _assets
│   │   │   │   │   │   │   └── icon.svg
│   │   │   │   │   │   ├── maths.py
│   │   │   │   │   │   ├── maths.yaml
│   │   │   │   │   │   └── tools
│   │   │   │   │   │       ├── eval_expression.py
│   │   │   │   │   │       └── eval_expression.yaml
│   │   │   │   │   ├── openweather
│   │   │   │   │   │   ├── _assets
│   │   │   │   │   │   │   └── icon.svg
│   │   │   │   │   │   ├── openweather.py
│   │   │   │   │   │   ├── openweather.yaml
│   │   │   │   │   │   └── tools
│   │   │   │   │   │       ├── weather.py
│   │   │   │   │   │       └── weather.yaml
│   │   │   │   │   ├── pubmed
│   │   │   │   │   │   ├── _assets
│   │   │   │   │   │   │   └── icon.svg
│   │   │   │   │   │   ├── pubmed.py
│   │   │   │   │   │   ├── pubmed.yaml
│   │   │   │   │   │   └── tools
│   │   │   │   │   │       ├── pubmed_search.py
│   │   │   │   │   │       └── pubmed_search.yaml
│   │   │   │   │   ├── qrcode
│   │   │   │   │   │   ├── _assets
│   │   │   │   │   │   │   └── icon.svg
│   │   │   │   │   │   ├── qrcode.py
│   │   │   │   │   │   ├── qrcode.yaml
│   │   │   │   │   │   └── tools
│   │   │   │   │   │       ├── qrcode_generator.py
│   │   │   │   │   │       └── qrcode_generator.yaml
│   │   │   │   │   ├── searxng
│   │   │   │   │   │   ├── _assets
│   │   │   │   │   │   │   └── icon.svg
│   │   │   │   │   │   ├── searxng.py
│   │   │   │   │   │   ├── searxng.yaml
│   │   │   │   │   │   └── tools
│   │   │   │   │   │       ├── searxng_search.py
│   │   │   │   │   │       └── searxng_search.yaml
│   │   │   │   │   ├── slack
│   │   │   │   │   │   ├── _assets
│   │   │   │   │   │   │   └── icon.svg
│   │   │   │   │   │   ├── slack.py
│   │   │   │   │   │   ├── slack.yaml
│   │   │   │   │   │   └── tools
│   │   │   │   │   │       ├── slack_webhook.py
│   │   │   │   │   │       └── slack_webhook.yaml
│   │   │   │   │   ├── spark
│   │   │   │   │   │   ├── __init__.py
│   │   │   │   │   │   ├── _assets
│   │   │   │   │   │   │   └── icon.svg
│   │   │   │   │   │   ├── spark.py
│   │   │   │   │   │   ├── spark.yaml
│   │   │   │   │   │   └── tools
│   │   │   │   │   │       ├── spark_img_generation.py
│   │   │   │   │   │       └── spark_img_generation.yaml
│   │   │   │   │   ├── stability
│   │   │   │   │   │   ├── _assets
│   │   │   │   │   │   │   └── icon.svg
│   │   │   │   │   │   ├── stability.py
│   │   │   │   │   │   ├── stability.yaml
│   │   │   │   │   │   └── tools
│   │   │   │   │   │       ├── base.py
│   │   │   │   │   │       ├── text2image.py
│   │   │   │   │   │       └── text2image.yaml
│   │   │   │   │   ├── stablediffusion
│   │   │   │   │   │   ├── _assets
│   │   │   │   │   │   │   └── icon.png
│   │   │   │   │   │   ├── stablediffusion.py
│   │   │   │   │   │   ├── stablediffusion.yaml
│   │   │   │   │   │   └── tools
│   │   │   │   │   │       ├── stable_diffusion.py
│   │   │   │   │   │       └── stable_diffusion.yaml
│   │   │   │   │   ├── stackexchange
│   │   │   │   │   │   ├── _assets
│   │   │   │   │   │   │   └── icon.svg
│   │   │   │   │   │   ├── stackexchange.py
│   │   │   │   │   │   ├── stackexchange.yaml
│   │   │   │   │   │   └── tools
│   │   │   │   │   │       ├── fetchAnsByStackExQuesID.py
│   │   │   │   │   │       ├── fetchAnsByStackExQuesID.yaml
│   │   │   │   │   │       ├── searchStackExQuestions.py
│   │   │   │   │   │       └── searchStackExQuestions.yaml
│   │   │   │   │   ├── tavily
│   │   │   │   │   │   ├── _assets
│   │   │   │   │   │   │   └── icon.png
│   │   │   │   │   │   ├── tavily.py
│   │   │   │   │   │   ├── tavily.yaml
│   │   │   │   │   │   └── tools
│   │   │   │   │   │       ├── tavily_search.py
│   │   │   │   │   │       └── tavily_search.yaml
│   │   │   │   │   ├── time
│   │   │   │   │   │   ├── _assets
│   │   │   │   │   │   │   └── icon.svg
│   │   │   │   │   │   ├── time.py
│   │   │   │   │   │   ├── time.yaml
│   │   │   │   │   │   └── tools
│   │   │   │   │   │       ├── current_time.py
│   │   │   │   │   │       ├── current_time.yaml
│   │   │   │   │   │       ├── weekday.py
│   │   │   │   │   │       └── weekday.yaml
│   │   │   │   │   ├── trello
│   │   │   │   │   │   ├── _assets
│   │   │   │   │   │   │   └── icon.svg
│   │   │   │   │   │   ├── tools
│   │   │   │   │   │   │   ├── create_board.py
│   │   │   │   │   │   │   ├── create_board.yaml
│   │   │   │   │   │   │   ├── create_list_on_board.py
│   │   │   │   │   │   │   ├── create_list_on_board.yaml
│   │   │   │   │   │   │   ├── create_new_card_on_board.py
│   │   │   │   │   │   │   ├── create_new_card_on_board.yaml
│   │   │   │   │   │   │   ├── delete_board.py
│   │   │   │   │   │   │   ├── delete_board.yaml
│   │   │   │   │   │   │   ├── delete_card.py
│   │   │   │   │   │   │   ├── delete_card.yaml
│   │   │   │   │   │   │   ├── fetch_all_boards.py
│   │   │   │   │   │   │   ├── fetch_all_boards.yaml
│   │   │   │   │   │   │   ├── get_board_actions.py
│   │   │   │   │   │   │   ├── get_board_actions.yaml
│   │   │   │   │   │   │   ├── get_board_by_id.py
│   │   │   │   │   │   │   ├── get_board_by_id.yaml
│   │   │   │   │   │   │   ├── get_board_cards.py
│   │   │   │   │   │   │   ├── get_board_cards.yaml
│   │   │   │   │   │   │   ├── get_filterd_board_cards.py
│   │   │   │   │   │   │   ├── get_filterd_board_cards.yaml
│   │   │   │   │   │   │   ├── get_lists_on_board.py
│   │   │   │   │   │   │   ├── get_lists_on_board.yaml
│   │   │   │   │   │   │   ├── update_board.py
│   │   │   │   │   │   │   ├── update_board.yaml
│   │   │   │   │   │   │   ├── update_card.py
│   │   │   │   │   │   │   └── update_card.yaml
│   │   │   │   │   │   ├── trello.py
│   │   │   │   │   │   └── trello.yaml
│   │   │   │   │   ├── twilio
│   │   │   │   │   │   ├── _assets
│   │   │   │   │   │   │   └── icon.svg
│   │   │   │   │   │   ├── tools
│   │   │   │   │   │   │   ├── send_message.py
│   │   │   │   │   │   │   └── send_message.yaml
│   │   │   │   │   │   ├── twilio.py
│   │   │   │   │   │   └── twilio.yaml
│   │   │   │   │   ├── vectorizer
│   │   │   │   │   │   ├── _assets
│   │   │   │   │   │   │   └── icon.png
│   │   │   │   │   │   ├── tools
│   │   │   │   │   │   │   ├── test_data.py
│   │   │   │   │   │   │   ├── vectorizer.py
│   │   │   │   │   │   │   └── vectorizer.yaml
│   │   │   │   │   │   ├── vectorizer.py
│   │   │   │   │   │   └── vectorizer.yaml
│   │   │   │   │   ├── webscraper
│   │   │   │   │   │   ├── _assets
│   │   │   │   │   │   │   └── icon.svg
│   │   │   │   │   │   ├── tools
│   │   │   │   │   │   │   ├── webscraper.py
│   │   │   │   │   │   │   └── webscraper.yaml
│   │   │   │   │   │   ├── webscraper.py
│   │   │   │   │   │   └── webscraper.yaml
│   │   │   │   │   ├── wecom
│   │   │   │   │   │   ├── _assets
│   │   │   │   │   │   │   └── icon.png
│   │   │   │   │   │   ├── tools
│   │   │   │   │   │   │   ├── wecom_group_bot.py
│   │   │   │   │   │   │   └── wecom_group_bot.yaml
│   │   │   │   │   │   ├── wecom.py
│   │   │   │   │   │   └── wecom.yaml
│   │   │   │   │   ├── wikipedia
│   │   │   │   │   │   ├── _assets
│   │   │   │   │   │   │   └── icon.svg
│   │   │   │   │   │   ├── tools
│   │   │   │   │   │   │   ├── wikipedia_search.py
│   │   │   │   │   │   │   └── wikipedia_search.yaml
│   │   │   │   │   │   ├── wikipedia.py
│   │   │   │   │   │   └── wikipedia.yaml
│   │   │   │   │   ├── wolframalpha
│   │   │   │   │   │   ├── _assets
│   │   │   │   │   │   │   └── icon.svg
│   │   │   │   │   │   ├── tools
│   │   │   │   │   │   │   ├── wolframalpha.py
│   │   │   │   │   │   │   └── wolframalpha.yaml
│   │   │   │   │   │   ├── wolframalpha.py
│   │   │   │   │   │   └── wolframalpha.yaml
│   │   │   │   │   ├── yahoo
│   │   │   │   │   │   ├── _assets
│   │   │   │   │   │   │   └── icon.png
│   │   │   │   │   │   ├── tools
│   │   │   │   │   │   │   ├── analytics.py
│   │   │   │   │   │   │   ├── analytics.yaml
│   │   │   │   │   │   │   ├── news.py
│   │   │   │   │   │   │   ├── news.yaml
│   │   │   │   │   │   │   ├── ticker.py
│   │   │   │   │   │   │   └── ticker.yaml
│   │   │   │   │   │   ├── yahoo.py
│   │   │   │   │   │   └── yahoo.yaml
│   │   │   │   │   └── youtube
│   │   │   │   │       ├── _assets
│   │   │   │   │       │   └── icon.svg
│   │   │   │   │       ├── tools
│   │   │   │   │       │   ├── videos.py
│   │   │   │   │       │   └── videos.yaml
│   │   │   │   │       ├── youtube.py
│   │   │   │   │       └── youtube.yaml
│   │   │   │   ├── builtin_tool_provider.py
│   │   │   │   └── tool_provider.py
│   │   │   ├── tool
│   │   │   │   ├── api_tool.py
│   │   │   │   ├── builtin_tool.py
│   │   │   │   ├── dataset_retriever
│   │   │   │   │   ├── dataset_multi_retriever_tool.py
│   │   │   │   │   ├── dataset_retriever_base_tool.py
│   │   │   │   │   └── dataset_retriever_tool.py
│   │   │   │   ├── dataset_retriever_tool.py
│   │   │   │   └── tool.py
│   │   │   ├── tool_engine.py
│   │   │   ├── tool_file_manager.py
│   │   │   ├── tool_manager.py
│   │   │   └── utils
│   │   │       ├── configuration.py
│   │   │       ├── message_transformer.py
│   │   │       ├── parser.py
│   │   │       ├── uuid_utils.py
│   │   │       └── web_reader_tool.py
│   │   ├── utils
│   │   │   ├── module_import_helper.py
│   │   │   └── position_helper.py
│   │   └── workflow
│   │       ├── __init__.py
│   │       ├── callbacks
│   │       │   ├── __init__.py
│   │       │   └── base_workflow_callback.py
│   │       ├── entities
│   │       │   ├── __init__.py
│   │       │   ├── base_node_data_entities.py
│   │       │   ├── node_entities.py
│   │       │   ├── variable_entities.py
│   │       │   ├── variable_pool.py
│   │       │   └── workflow_entities.py
│   │       ├── errors.py
│   │       ├── nodes
│   │       │   ├── __init__.py
│   │       │   ├── answer
│   │       │   │   ├── __init__.py
│   │       │   │   ├── answer_node.py
│   │       │   │   └── entities.py
│   │       │   ├── base_node.py
│   │       │   ├── code
│   │       │   │   ├── __init__.py
│   │       │   │   ├── code_node.py
│   │       │   │   └── entities.py
│   │       │   ├── end
│   │       │   │   ├── __init__.py
│   │       │   │   ├── end_node.py
│   │       │   │   └── entities.py
│   │       │   ├── http_request
│   │       │   │   ├── __init__.py
│   │       │   │   ├── entities.py
│   │       │   │   ├── http_executor.py
│   │       │   │   └── http_request_node.py
│   │       │   ├── if_else
│   │       │   │   ├── __init__.py
│   │       │   │   ├── entities.py
│   │       │   │   └── if_else_node.py
│   │       │   ├── knowledge_retrieval
│   │       │   │   ├── __init__.py
│   │       │   │   ├── entities.py
│   │       │   │   └── knowledge_retrieval_node.py
│   │       │   ├── llm
│   │       │   │   ├── __init__.py
│   │       │   │   ├── entities.py
│   │       │   │   └── llm_node.py
│   │       │   ├── question_classifier
│   │       │   │   ├── __init__.py
│   │       │   │   ├── entities.py
│   │       │   │   ├── question_classifier_node.py
│   │       │   │   └── template_prompts.py
│   │       │   ├── start
│   │       │   │   ├── __init__.py
│   │       │   │   ├── entities.py
│   │       │   │   └── start_node.py
│   │       │   ├── template_transform
│   │       │   │   ├── __init__.py
│   │       │   │   ├── entities.py
│   │       │   │   └── template_transform_node.py
│   │       │   ├── tool
│   │       │   │   ├── __init__.py
│   │       │   │   ├── entities.py
│   │       │   │   └── tool_node.py
│   │       │   └── variable_assigner
│   │       │       ├── __init__.py
│   │       │       ├── entities.py
│   │       │       └── variable_assigner_node.py
│   │       ├── utils
│   │       │   ├── __init__.py
│   │       │   └── variable_template_parser.py
│   │       └── workflow_engine_manager.py
│   ├── docker
│   │   └── entrypoint.sh
│   ├── events
│   │   ├── app_event.py
│   │   ├── dataset_event.py
│   │   ├── document_event.py
│   │   ├── event_handlers
│   │   │   ├── __init__.py
│   │   │   ├── clean_when_dataset_deleted.py
│   │   │   ├── clean_when_document_deleted.py
│   │   │   ├── create_document_index.py
│   │   │   ├── create_installed_app_when_app_created.py
│   │   │   ├── create_site_record_when_app_created.py
│   │   │   ├── deduct_quota_when_messaeg_created.py
│   │   │   ├── delete_installed_app_when_app_deleted.py
│   │   │   ├── delete_tool_parameters_cache_when_sync_draft_workflow.py
│   │   │   ├── document_index_event.py
│   │   │   ├── update_app_dataset_join_when_app_model_config_updated.py
│   │   │   ├── update_app_dataset_join_when_app_published_workflow_updated.py
│   │   │   └── update_provider_last_used_at_when_messaeg_created.py
│   │   ├── message_event.py
│   │   └── tenant_event.py
│   ├── extensions
│   │   ├── ext_celery.py
│   │   ├── ext_code_based_extension.py
│   │   ├── ext_compress.py
│   │   ├── ext_database.py
│   │   ├── ext_hosting_provider.py
│   │   ├── ext_login.py
│   │   ├── ext_mail.py
│   │   ├── ext_migrate.py
│   │   ├── ext_redis.py
│   │   ├── ext_sentry.py
│   │   ├── ext_storage.py
│   │   └── storage
│   │       ├── aliyun_storage.py
│   │       ├── azure_storage.py
│   │       ├── base_storage.py
│   │       ├── google_storage.py
│   │       ├── local_storage.py
│   │       └── s3_storage.py
│   ├── fields
│   │   ├── __init__.py
│   │   ├── annotation_fields.py
│   │   ├── api_based_extension_fields.py
│   │   ├── app_fields.py
│   │   ├── conversation_fields.py
│   │   ├── data_source_fields.py
│   │   ├── dataset_fields.py
│   │   ├── document_fields.py
│   │   ├── end_user_fields.py
│   │   ├── file_fields.py
│   │   ├── hit_testing_fields.py
│   │   ├── installed_app_fields.py
│   │   ├── member_fields.py
│   │   ├── message_fields.py
│   │   ├── segment_fields.py
│   │   ├── tag_fields.py
│   │   ├── workflow_app_log_fields.py
│   │   ├── workflow_fields.py
│   │   └── workflow_run_fields.py
│   ├── libs
│   │   ├── __init__.py
│   │   ├── exception.py
│   │   ├── external_api.py
│   │   ├── gmpy2_pkcs10aep_cipher.py
│   │   ├── helper.py
│   │   ├── infinite_scroll_pagination.py
│   │   ├── json_in_md_parser.py
│   │   ├── login.py
│   │   ├── oauth.py
│   │   ├── oauth_data_source.py
│   │   ├── passport.py
│   │   ├── password.py
│   │   ├── rsa.py
│   │   └── smtp.py
│   ├── mabos
│   │   ├── agents
│   │   │   └── {agent_id}
│   │   │       ├── communication_api.py
│   │   │       ├── execution_api.py
│   │   │       ├── plans_api.py
│   │   │       └── reasoning_api.py
│   │   ├── agents_api.py
│   │   ├── knowledge-graph_api.py
│   │   └── ontologies_api.py
│   ├── migrations
│   │   ├── README
│   │   ├── alembic.ini
│   │   ├── env.py
│   │   ├── script.py.mako
│   │   └── versions
│   │       ├── 00bacef91f18_rename_api_provider_description.py
│   │       ├── 053da0c1d756_add_api_tool_privacy.py
│   │       ├── 114eed84c228_remove_tool_id_from_model_invoke.py
│   │       ├── 16830a790f0f_.py
│   │       ├── 16fa53d9faec_add_provider_model_support.py
│   │       ├── 17b5ab037c40_add_keyworg_table_storage_type.py
│   │       ├── 187385f442fc_modify_provider_model_name_length.py
│   │       ├── 23db93619b9d_add_message_files_into_agent_thought.py
│   │       ├── 246ba09cbbdb_add_app_anntation_setting.py
│   │       ├── 2beac44e5f5f_add_is_universal_in_apps.py
│   │       ├── 2c8af9671032_add_qa_document_language.py
│   │       ├── 2e9819ca5b28_add_tenant_id_in_api_token.py
│   │       ├── 380c6aa5a70d_add_tool_labels_to_agent_thought.py
│   │       ├── 3c7cac9521c6_add_tags_and_binding_table.py
│   │       ├── 3ef9b2b6bee6_add_assistant_app.py
│   │       ├── 42e85ed5564d_conversation_columns_set_nullable.py
│   │       ├── 46976cc39132_add_annotation_histoiry_score.py
│   │       ├── 47cc7df8c4f3_modify_default_model_name_length.py
│   │       ├── 4823da1d26cf_add_tool_file.py
│   │       ├── 4829e54d2fee_change_message_chain_id_to_nullable.py
│   │       ├── 4bcffcd64aa4_update_dataset_model_field_null_.py
│   │       ├── 5022897aaceb_add_model_name_in_embedding.py
│   │       ├── 563cf8bf777b_enable_tool_file_without_conversation_id.py
│   │       ├── 614f77cecc48_add_last_active_at.py
│   │       ├── 64b051264f32_init.py
│   │       ├── 6dcb43972bdc_add_dataset_retriever_resource.py
│   │       ├── 6e2cfb077b04_add_dataset_collection_binding.py
│   │       ├── 714aafe25d39_add_anntation_history_match_response.py
│   │       ├── 77e83833755c_add_app_config_retriever_resource.py
│   │       ├── 7ce5a52e4eee_add_tool_providers.py
│   │       ├── 853f9b9cd3b6_add_message_price_unit.py
│   │       ├── 88072f0caa04_add_custom_config_in_tenant.py
│   │       ├── 89c7899ca936_.py
│   │       ├── 8ae9bc661daa_add_tool_conversation_variables_idx.py
│   │       ├── 8d2d099ceb74_add_qa_model_support.py
│   │       ├── 8ec536f3c800_rename_api_provider_credentails.py
│   │       ├── 8fe468ba0ca5_add_gpt4v_supports.py
│   │       ├── 968fff4c0ab9_add_api_based_extension.py
│   │       ├── 9f4e3427ea84_add_created_by_role.py
│   │       ├── 9fafbd60eca1_add_message_file_belongs_to.py
│   │       ├── a45f4dfde53b_add_language_to_recommend_apps.py
│   │       ├── a5b56fb053ef_app_config_add_speech_to_text.py
│   │       ├── a8d7385a7b66_add_embeddings_provider_name.py
│   │       ├── a8f9b3c45e4a_add_tenant_id_db_index.py
│   │       ├── a9836e3baeee_add_external_data_tools_in_app_model_.py
│   │       ├── ab23c11305d4_add_dataset_query_variable_at_app_model_.py
│   │       ├── ad472b61a054_add_api_provider_icon.py
│   │       ├── b24be59fbb04_.py
│   │       ├── b289e2408ee2_add_workflow.py
│   │       ├── b3a09c049e8e_add_advanced_prompt_templates.py
│   │       ├── b5429b71023c_messages_columns_set_nullable.py
│   │       ├── bf0aec5ba2cf_add_provider_order.py
│   │       ├── c3311b089690_add_tool_meta.py
│   │       ├── c71211c8f604_add_tool_invoke_model_log.py
│   │       ├── cc04d0998d4d_set_model_config_column_nullable.py
│   │       ├── d3d503a3471c_add_is_deleted_to_conversations.py
│   │       ├── de95f5c77138_migration_serpapi_api_key.py
│   │       ├── dfb3b7f477da_add_tool_index.py
│   │       ├── e1901f623fd0_add_annotation_reply.py
│   │       ├── e2eacc9a1b63_add_status_for_message.py
│   │       ├── e32f6ccb87c6_e08af0a69ccefbb59fa80c778efee300bb780980.py
│   │       ├── e35ed59becda_modify_quota_limit_field_type.py
│   │       ├── e8883b0148c9_add_dataset_model_name.py
│   │       ├── f25003750af4_add_created_updated_at.py
│   │       ├── f2a6fc85e260_add_anntation_history_message_id.py
│   │       ├── f9107f83abab_add_desc_for_apps.py
│   │       └── fca025d3b60f_add_dataset_retrival_model.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── account.py
│   │   ├── api_based_extension.py
│   │   ├── dataset.py
│   │   ├── mabos
│   │   │   ├── __init__.py
│   │   │   ├── agent.py
│   │   │   ├── communication.py
│   │   │   ├── execution.py
│   │   │   ├── knowledge_graph.py
│   │   │   ├── ontology_api.py
│   │   │   ├── planning.py
│   │   │   └── reasoning.py
│   │   ├── model.py
│   │   ├── provider.py
│   │   ├── source.py
│   │   ├── task.py
│   │   ├── tool.py
│   │   ├── tools.py
│   │   ├── web.py
│   │   └── workflow.py
│   ├── pyproject.toml
│   ├── requirements-dev.txt
│   ├── requirements.txt
│   ├── routers
│   │   └── mabos.py
│   ├── schedule
│   │   ├── clean_embedding_cache_task.py
│   │   └── clean_unused_datasets_task.py
│   ├── services
│   │   ├── __init__.py
│   │   ├── account_service.py
│   │   ├── advanced_prompt_template_service.py
│   │   ├── agent_service.py
│   │   ├── annotation_service.py
│   │   ├── api_based_extension_service.py
│   │   ├── app_generate_service.py
│   │   ├── app_model_config_service.py
│   │   ├── app_service.py
│   │   ├── audio_service.py
│   │   ├── billing_service.py
│   │   ├── code_based_extension_service.py
│   │   ├── conversation_service.py
│   │   ├── dataset_service.py
│   │   ├── enterprise
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   └── enterprise_service.py
│   │   ├── entities
│   │   │   ├── __init__.py
│   │   │   └── model_provider_entities.py
│   │   ├── errors
│   │   │   ├── __init__.py
│   │   │   ├── account.py
│   │   │   ├── app.py
│   │   │   ├── app_model_config.py
│   │   │   ├── audio.py
│   │   │   ├── base.py
│   │   │   ├── completion.py
│   │   │   ├── conversation.py
│   │   │   ├── dataset.py
│   │   │   ├── document.py
│   │   │   ├── file.py
│   │   │   ├── index.py
│   │   │   └── message.py
│   │   ├── feature_service.py
│   │   ├── file_service.py
│   │   ├── hit_testing_service.py
│   │   ├── mabos_service.py
│   │   ├── message_service.py
│   │   ├── model_provider_service.py
│   │   ├── moderation_service.py
│   │   ├── operation_service.py
│   │   ├── recommended_app_service.py
│   │   ├── saved_message_service.py
│   │   ├── tag_service.py
│   │   ├── tools_manage_service.py
│   │   ├── tools_transform_service.py
│   │   ├── vector_service.py
│   │   ├── web_conversation_service.py
│   │   ├── workflow
│   │   │   ├── __init__.py
│   │   │   └── workflow_converter.py
│   │   ├── workflow_app_service.py
│   │   ├── workflow_run_service.py
│   │   ├── workflow_service.py
│   │   └── workspace_service.py
│   ├── tasks
│   │   ├── add_document_to_index_task.py
│   │   ├── annotation
│   │   │   ├── add_annotation_to_index_task.py
│   │   │   ├── batch_import_annotations_task.py
│   │   │   ├── delete_annotation_index_task.py
│   │   │   ├── disable_annotation_reply_task.py
│   │   │   ├── enable_annotation_reply_task.py
│   │   │   └── update_annotation_to_index_task.py
│   │   ├── batch_create_segment_to_index_task.py
│   │   ├── clean_dataset_task.py
│   │   ├── clean_document_task.py
│   │   ├── clean_notion_document_task.py
│   │   ├── create_segment_to_index_task.py
│   │   ├── deal_dataset_vector_index_task.py
│   │   ├── delete_segment_from_index_task.py
│   │   ├── disable_segment_from_index_task.py
│   │   ├── document_indexing_sync_task.py
│   │   ├── document_indexing_task.py
│   │   ├── document_indexing_update_task.py
│   │   ├── duplicate_document_indexing_task.py
│   │   ├── enable_segment_to_index_task.py
│   │   ├── mail_invite_member_task.py
│   │   ├── recover_document_indexing_task.py
│   │   ├── remove_document_from_index_task.py
│   │   └── retry_document_indexing_task.py
│   ├── templates
│   │   ├── invite_member_mail_template_en-US.html
│   │   └── invite_member_mail_template_zh-CN.html
│   └── tests
│       ├── __init__.py
│       ├── integration_tests
│       │   ├── __init__.py
│       │   ├── conftest.py
│       │   ├── model_runtime
│       │   │   ├── __init__.py
│       │   │   ├── __mock
│       │   │   │   ├── anthropic.py
│       │   │   │   ├── google.py
│       │   │   │   ├── huggingface.py
│       │   │   │   ├── huggingface_chat.py
│       │   │   │   ├── openai.py
│       │   │   │   ├── openai_chat.py
│       │   │   │   ├── openai_completion.py
│       │   │   │   ├── openai_embeddings.py
│       │   │   │   ├── openai_moderation.py
│       │   │   │   ├── openai_remote.py
│       │   │   │   ├── openai_speech2text.py
│       │   │   │   └── xinference.py
│       │   │   ├── anthropic
│       │   │   │   ├── __init__.py
│       │   │   │   ├── test_llm.py
│       │   │   │   └── test_provider.py
│       │   │   ├── assets
│       │   │   │   └── audio.mp3
│       │   │   ├── azure_openai
│       │   │   │   ├── __init__.py
│       │   │   │   ├── test_llm.py
│       │   │   │   └── test_text_embedding.py
│       │   │   ├── baichuan
│       │   │   │   ├── __init__.py
│       │   │   │   ├── test_llm.py
│       │   │   │   ├── test_provider.py
│       │   │   │   └── test_text_embedding.py
│       │   │   ├── bedrock
│       │   │   │   ├── __init__.py
│       │   │   │   ├── test_llm.py
│       │   │   │   └── test_provider.py
│       │   │   ├── chatglm
│       │   │   │   ├── __init__.py
│       │   │   │   ├── test_llm.py
│       │   │   │   └── test_provider.py
│       │   │   ├── cohere
│       │   │   │   ├── __init__.py
│       │   │   │   ├── test_llm.py
│       │   │   │   ├── test_provider.py
│       │   │   │   ├── test_rerank.py
│       │   │   │   └── test_text_embedding.py
│       │   │   ├── google
│       │   │   │   ├── __init__.py
│       │   │   │   ├── test_llm.py
│       │   │   │   └── test_provider.py
│       │   │   ├── huggingface_hub
│       │   │   │   ├── __init__.py
│       │   │   │   ├── test_llm.py
│       │   │   │   └── test_text_embedding.py
│       │   │   ├── jina
│       │   │   │   ├── __init__.py
│       │   │   │   ├── test_provider.py
│       │   │   │   └── test_text_embedding.py
│       │   │   ├── localai
│       │   │   │   ├── __init__.py
│       │   │   │   ├── test_embedding.py
│       │   │   │   ├── test_llm.py
│       │   │   │   ├── test_rerank.py
│       │   │   │   └── test_speech2text.py
│       │   │   ├── minimax
│       │   │   │   ├── __init__.py
│       │   │   │   ├── test_embedding.py
│       │   │   │   ├── test_llm.py
│       │   │   │   └── test_provider.py
│       │   │   ├── ollama
│       │   │   │   ├── __init__.py
│       │   │   │   ├── test_llm.py
│       │   │   │   └── test_text_embedding.py
│       │   │   ├── openai
│       │   │   │   ├── __init__.py
│       │   │   │   ├── test_llm.py
│       │   │   │   ├── test_moderation.py
│       │   │   │   ├── test_provider.py
│       │   │   │   ├── test_speech2text.py
│       │   │   │   └── test_text_embedding.py
│       │   │   ├── openai_api_compatible
│       │   │   │   ├── __init__.py
│       │   │   │   ├── test_llm.py
│       │   │   │   └── test_text_embedding.py
│       │   │   ├── openllm
│       │   │   │   ├── __init__.py
│       │   │   │   ├── test_embedding.py
│       │   │   │   └── test_llm.py
│       │   │   ├── openrouter
│       │   │   │   ├── __init__.py
│       │   │   │   └── test_llm.py
│       │   │   ├── replicate
│       │   │   │   ├── __init__.py
│       │   │   │   ├── test_llm.py
│       │   │   │   └── test_text_embedding.py
│       │   │   ├── spark
│       │   │   │   ├── __init__.py
│       │   │   │   ├── test_llm.py
│       │   │   │   └── test_provider.py
│       │   │   ├── test_model_provider_factory.py
│       │   │   ├── togetherai
│       │   │   │   ├── __init__.py
│       │   │   │   └── test_llm.py
│       │   │   ├── tongyi
│       │   │   │   ├── __init__.py
│       │   │   │   ├── test_llm.py
│       │   │   │   └── test_provider.py
│       │   │   ├── volcengine_maas
│       │   │   │   ├── __init__.py
│       │   │   │   ├── test_embedding.py
│       │   │   │   └── test_llm.py
│       │   │   ├── wenxin
│       │   │   │   ├── __init__.py
│       │   │   │   ├── test_llm.py
│       │   │   │   └── test_provider.py
│       │   │   ├── xinference
│       │   │   │   ├── __init__.py
│       │   │   │   ├── test_embeddings.py
│       │   │   │   ├── test_llm.py
│       │   │   │   └── test_rerank.py
│       │   │   └── zhipuai
│       │   │       ├── __init__.py
│       │   │       ├── test_llm.py
│       │   │       ├── test_provider.py
│       │   │       └── test_text_embedding.py
│       │   ├── tools
│       │   │   ├── __init__.py
│       │   │   ├── __mock_server
│       │   │   │   └── openapi_todo.py
│       │   │   ├── code
│       │   │   │   └── __init__.py
│       │   │   └── test_all_provider.py
│       │   ├── utils
│       │   │   ├── child_class.py
│       │   │   ├── lazy_load_class.py
│       │   │   ├── parent_class.py
│       │   │   └── test_module_import_helper.py
│       │   ├── vdb
│       │   │   ├── __init__.py
│       │   │   ├── milvus
│       │   │   │   ├── __init__.py
│       │   │   │   └── test_milvus.py
│       │   │   ├── pgvecto_rs
│       │   │   │   ├── __init__.py
│       │   │   │   └── test_pgvecto_rs.py
│       │   │   ├── pgvector
│       │   │   │   ├── __init__.py
│       │   │   │   └── test_pgvector.py
│       │   │   ├── qdrant
│       │   │   │   ├── __init__.py
│       │   │   │   └── test_qdrant.py
│       │   │   ├── test_vector_store.py
│       │   │   └── weaviate
│       │   │       ├── __init__.py
│       │   │       └── test_weaviate.py
│       │   └── workflow
│       │       ├── __init__.py
│       │       └── nodes
│       │           ├── __init__.py
│       │           ├── __mock
│       │           │   ├── code_executor.py
│       │           │   └── http.py
│       │           ├── code_executor
│       │           │   ├── __init__.py
│       │           │   ├── test_code_executor.py
│       │           │   ├── test_code_javascript.py
│       │           │   ├── test_code_jinja2.py
│       │           │   └── test_code_python3.py
│       │           ├── test_code.py
│       │           ├── test_http.py
│       │           ├── test_llm.py
│       │           ├── test_template_transform.py
│       │           └── test_tool.py
│       └── unit_tests
│           ├── __init__.py
│           ├── conftest.py
│           ├── core
│           │   ├── __init__.py
│           │   ├── prompt
│           │   │   ├── __init__.py
│           │   │   ├── test_advanced_prompt_transform.py
│           │   │   ├── test_prompt_transform.py
│           │   │   └── test_simple_prompt_transform.py
│           │   ├── rag
│           │   │   ├── __init__.py
│           │   │   └── datasource
│           │   │       ├── __init__.py
│           │   │       └── vdb
│           │   │           ├── __init__.py
│           │   │           └── milvus
│           │   │               └── test_milvus.py
│           │   └── workflow
│           │       ├── __init__.py
│           │       └── nodes
│           │           ├── __init__.py
│           │           ├── test_answer.py
│           │           └── test_if_else.py
│           ├── libs
│           │   ├── test_rsa.py
│           │   └── test_yarl.py
│           ├── models
│           │   └── test_account.py
│           └── services
│               ├── __init__.py
│               └── workflow
│                   ├── __init__.py
│                   └── test_workflow_converter.py
├── dev
│   ├── pytest
│   │   ├── pytest_all_tests.sh
│   │   ├── pytest_model_runtime.sh
│   │   ├── pytest_tools.sh
│   │   ├── pytest_unit_tests.sh
│   │   ├── pytest_vdb.sh
│   │   └── pytest_workflow.sh
│   └── reformat
├── docker
│   ├── docker-compose.middleware.yaml
│   ├── docker-compose.milvus.yaml
│   ├── docker-compose.pgvecto-rs.yaml
│   ├── docker-compose.pgvector.yaml
│   ├── docker-compose.png
│   ├── docker-compose.qdrant.yaml
│   ├── docker-compose.yaml
│   ├── nginx
│   │   ├── conf.d
│   │   │   └── default.conf
│   │   ├── nginx.conf
│   │   ├── proxy.conf
│   │   └── ssl
│   └── volumes
│       ├── app
│       │   └── storage
│       │       └── privkeys
│       │           └── 70683c39-0cf2-4b59-9059-e7f14a944865
│       │               └── private.pem
│       ├── db
│       │   └── data
│       │       └── pgdata
│       │           ├── PG_VERSION
│       │           ├── base
│       │           │   ├── 1
│       │           │   │   ├── 112
│       │           │   │   ├── 113
│       │           │   │   ├── 1247
│       │           │   │   ├── 1247_fsm
│       │           │   │   ├── 1247_vm
│       │           │   │   ├── 1249
│       │           │   │   ├── 1249_fsm
│       │           │   │   ├── 1249_vm
│       │           │   │   ├── 1255
│       │           │   │   ├── 1255_fsm
│       │           │   │   ├── 1255_vm
│       │           │   │   ├── 1259
│       │           │   │   ├── 1259_fsm
│       │           │   │   ├── 1259_vm
│       │           │   │   ├── 13436
│       │           │   │   ├── 13436_fsm
│       │           │   │   ├── 13436_vm
│       │           │   │   ├── 13439
│       │           │   │   ├── 13440
│       │           │   │   ├── 13441
│       │           │   │   ├── 13441_fsm
│       │           │   │   ├── 13441_vm
│       │           │   │   ├── 13444
│       │           │   │   ├── 13445
│       │           │   │   ├── 13446
│       │           │   │   ├── 13446_fsm
│       │           │   │   ├── 13446_vm
│       │           │   │   ├── 13449
│       │           │   │   ├── 13450
│       │           │   │   ├── 13451
│       │           │   │   ├── 13451_fsm
│       │           │   │   ├── 13451_vm
│       │           │   │   ├── 13454
│       │           │   │   ├── 13455
│       │           │   │   ├── 1417
│       │           │   │   ├── 1418
│       │           │   │   ├── 174
│       │           │   │   ├── 175
│       │           │   │   ├── 2187
│       │           │   │   ├── 2224
│       │           │   │   ├── 2228
│       │           │   │   ├── 2328
│       │           │   │   ├── 2336
│       │           │   │   ├── 2337
│       │           │   │   ├── 2579
│       │           │   │   ├── 2600
│       │           │   │   ├── 2600_fsm
│       │           │   │   ├── 2600_vm
│       │           │   │   ├── 2601
│       │           │   │   ├── 2601_fsm
│       │           │   │   ├── 2601_vm
│       │           │   │   ├── 2602
│       │           │   │   ├── 2602_fsm
│       │           │   │   ├── 2602_vm
│       │           │   │   ├── 2603
│       │           │   │   ├── 2603_fsm
│       │           │   │   ├── 2603_vm
│       │           │   │   ├── 2604
│       │           │   │   ├── 2605
│       │           │   │   ├── 2605_fsm
│       │           │   │   ├── 2605_vm
│       │           │   │   ├── 2606
│       │           │   │   ├── 2606_fsm
│       │           │   │   ├── 2606_vm
│       │           │   │   ├── 2607
│       │           │   │   ├── 2607_fsm
│       │           │   │   ├── 2607_vm
│       │           │   │   ├── 2608
│       │           │   │   ├── 2608_fsm
│       │           │   │   ├── 2608_vm
│       │           │   │   ├── 2609
│       │           │   │   ├── 2609_fsm
│       │           │   │   ├── 2609_vm
│       │           │   │   ├── 2610
│       │           │   │   ├── 2610_fsm
│       │           │   │   ├── 2610_vm
│       │           │   │   ├── 2611
│       │           │   │   ├── 2612
│       │           │   │   ├── 2612_fsm
│       │           │   │   ├── 2612_vm
│       │           │   │   ├── 2613
│       │           │   │   ├── 2615
│       │           │   │   ├── 2615_fsm
│       │           │   │   ├── 2615_vm
│       │           │   │   ├── 2616
│       │           │   │   ├── 2616_fsm
│       │           │   │   ├── 2616_vm
│       │           │   │   ├── 2617
│       │           │   │   ├── 2617_fsm
│       │           │   │   ├── 2617_vm
│       │           │   │   ├── 2618
│       │           │   │   ├── 2618_fsm
│       │           │   │   ├── 2618_vm
│       │           │   │   ├── 2619
│       │           │   │   ├── 2619_fsm
│       │           │   │   ├── 2619_vm
│       │           │   │   ├── 2620
│       │           │   │   ├── 2650
│       │           │   │   ├── 2651
│       │           │   │   ├── 2652
│       │           │   │   ├── 2653
│       │           │   │   ├── 2654
│       │           │   │   ├── 2655
│       │           │   │   ├── 2656
│       │           │   │   ├── 2657
│       │           │   │   ├── 2658
│       │           │   │   ├── 2659
│       │           │   │   ├── 2660
│       │           │   │   ├── 2661
│       │           │   │   ├── 2662
│       │           │   │   ├── 2663
│       │           │   │   ├── 2664
│       │           │   │   ├── 2665
│       │           │   │   ├── 2666
│       │           │   │   ├── 2667
│       │           │   │   ├── 2668
│       │           │   │   ├── 2669
│       │           │   │   ├── 2670
│       │           │   │   ├── 2673
│       │           │   │   ├── 2674
│       │           │   │   ├── 2675
│       │           │   │   ├── 2678
│       │           │   │   ├── 2679
│       │           │   │   ├── 2680
│       │           │   │   ├── 2681
│       │           │   │   ├── 2682
│       │           │   │   ├── 2683
│       │           │   │   ├── 2684
│       │           │   │   ├── 2685
│       │           │   │   ├── 2686
│       │           │   │   ├── 2687
│       │           │   │   ├── 2688
│       │           │   │   ├── 2689
│       │           │   │   ├── 2690
│       │           │   │   ├── 2691
│       │           │   │   ├── 2692
│       │           │   │   ├── 2693
│       │           │   │   ├── 2696
│       │           │   │   ├── 2699
│       │           │   │   ├── 2701
│       │           │   │   ├── 2702
│       │           │   │   ├── 2703
│       │           │   │   ├── 2704
│       │           │   │   ├── 2753
│       │           │   │   ├── 2753_fsm
│       │           │   │   ├── 2753_vm
│       │           │   │   ├── 2754
│       │           │   │   ├── 2755
│       │           │   │   ├── 2756
│       │           │   │   ├── 2757
│       │           │   │   ├── 2830
│       │           │   │   ├── 2831
│       │           │   │   ├── 2832
│       │           │   │   ├── 2833
│       │           │   │   ├── 2834
│       │           │   │   ├── 2835
│       │           │   │   ├── 2836
│       │           │   │   ├── 2836_fsm
│       │           │   │   ├── 2836_vm
│       │           │   │   ├── 2837
│       │           │   │   ├── 2838
│       │           │   │   ├── 2838_fsm
│       │           │   │   ├── 2838_vm
│       │           │   │   ├── 2839
│       │           │   │   ├── 2840
│       │           │   │   ├── 2840_fsm
│       │           │   │   ├── 2840_vm
│       │           │   │   ├── 2841
│       │           │   │   ├── 2995
│       │           │   │   ├── 2996
│       │           │   │   ├── 3079
│       │           │   │   ├── 3079_fsm
│       │           │   │   ├── 3079_vm
│       │           │   │   ├── 3080
│       │           │   │   ├── 3081
│       │           │   │   ├── 3085
│       │           │   │   ├── 3118
│       │           │   │   ├── 3119
│       │           │   │   ├── 3164
│       │           │   │   ├── 3256
│       │           │   │   ├── 3257
│       │           │   │   ├── 3258
│       │           │   │   ├── 3350
│       │           │   │   ├── 3351
│       │           │   │   ├── 3379
│       │           │   │   ├── 3380
│       │           │   │   ├── 3381
│       │           │   │   ├── 3394
│       │           │   │   ├── 3394_fsm
│       │           │   │   ├── 3394_vm
│       │           │   │   ├── 3395
│       │           │   │   ├── 3429
│       │           │   │   ├── 3430
│       │           │   │   ├── 3431
│       │           │   │   ├── 3433
│       │           │   │   ├── 3439
│       │           │   │   ├── 3440
│       │           │   │   ├── 3455
│       │           │   │   ├── 3456
│       │           │   │   ├── 3456_fsm
│       │           │   │   ├── 3456_vm
│       │           │   │   ├── 3466
│       │           │   │   ├── 3467
│       │           │   │   ├── 3468
│       │           │   │   ├── 3501
│       │           │   │   ├── 3502
│       │           │   │   ├── 3503
│       │           │   │   ├── 3534
│       │           │   │   ├── 3541
│       │           │   │   ├── 3541_fsm
│       │           │   │   ├── 3541_vm
│       │           │   │   ├── 3542
│       │           │   │   ├── 3574
│       │           │   │   ├── 3575
│       │           │   │   ├── 3576
│       │           │   │   ├── 3596
│       │           │   │   ├── 3597
│       │           │   │   ├── 3598
│       │           │   │   ├── 3599
│       │           │   │   ├── 3600
│       │           │   │   ├── 3600_fsm
│       │           │   │   ├── 3600_vm
│       │           │   │   ├── 3601
│       │           │   │   ├── 3601_fsm
│       │           │   │   ├── 3601_vm
│       │           │   │   ├── 3602
│       │           │   │   ├── 3602_fsm
│       │           │   │   ├── 3602_vm
│       │           │   │   ├── 3603
│       │           │   │   ├── 3603_fsm
│       │           │   │   ├── 3603_vm
│       │           │   │   ├── 3604
│       │           │   │   ├── 3605
│       │           │   │   ├── 3606
│       │           │   │   ├── 3607
│       │           │   │   ├── 3608
│       │           │   │   ├── 3609
│       │           │   │   ├── 3712
│       │           │   │   ├── 3764
│       │           │   │   ├── 3764_fsm
│       │           │   │   ├── 3764_vm
│       │           │   │   ├── 3766
│       │           │   │   ├── 3767
│       │           │   │   ├── 3997
│       │           │   │   ├── 4143
│       │           │   │   ├── 4144
│       │           │   │   ├── 4145
│       │           │   │   ├── 4146
│       │           │   │   ├── 4147
│       │           │   │   ├── 4148
│       │           │   │   ├── 4149
│       │           │   │   ├── 4150
│       │           │   │   ├── 4151
│       │           │   │   ├── 4152
│       │           │   │   ├── 4153
│       │           │   │   ├── 4154
│       │           │   │   ├── 4155
│       │           │   │   ├── 4156
│       │           │   │   ├── 4157
│       │           │   │   ├── 4158
│       │           │   │   ├── 4159
│       │           │   │   ├── 4160
│       │           │   │   ├── 4163
│       │           │   │   ├── 4164
│       │           │   │   ├── 4165
│       │           │   │   ├── 4166
│       │           │   │   ├── 4167
│       │           │   │   ├── 4168
│       │           │   │   ├── 4169
│       │           │   │   ├── 4170
│       │           │   │   ├── 4171
│       │           │   │   ├── 4172
│       │           │   │   ├── 4173
│       │           │   │   ├── 4174
│       │           │   │   ├── 5002
│       │           │   │   ├── 548
│       │           │   │   ├── 549
│       │           │   │   ├── 6102
│       │           │   │   ├── 6104
│       │           │   │   ├── 6106
│       │           │   │   ├── 6110
│       │           │   │   ├── 6111
│       │           │   │   ├── 6112
│       │           │   │   ├── 6113
│       │           │   │   ├── 6116
│       │           │   │   ├── 6117
│       │           │   │   ├── 6175
│       │           │   │   ├── 6176
│       │           │   │   ├── 6228
│       │           │   │   ├── 6229
│       │           │   │   ├── 6237
│       │           │   │   ├── 6238
│       │           │   │   ├── 6239
│       │           │   │   ├── 826
│       │           │   │   ├── 827
│       │           │   │   ├── 828
│       │           │   │   ├── PG_VERSION
│       │           │   │   └── pg_filenode.map
│       │           │   ├── 16384
│       │           │   │   ├── 112
│       │           │   │   ├── 113
│       │           │   │   ├── 1247
│       │           │   │   ├── 1247_fsm
│       │           │   │   ├── 1247_vm
│       │           │   │   ├── 1249
│       │           │   │   ├── 1249_fsm
│       │           │   │   ├── 1249_vm
│       │           │   │   ├── 1255
│       │           │   │   ├── 1255_fsm
│       │           │   │   ├── 1255_vm
│       │           │   │   ├── 1259
│       │           │   │   ├── 1259_fsm
│       │           │   │   ├── 1259_vm
│       │           │   │   ├── 13436
│       │           │   │   ├── 13436_fsm
│       │           │   │   ├── 13436_vm
│       │           │   │   ├── 13439
│       │           │   │   ├── 13440
│       │           │   │   ├── 13441
│       │           │   │   ├── 13441_fsm
│       │           │   │   ├── 13441_vm
│       │           │   │   ├── 13444
│       │           │   │   ├── 13445
│       │           │   │   ├── 13446
│       │           │   │   ├── 13446_fsm
│       │           │   │   ├── 13446_vm
│       │           │   │   ├── 13449
│       │           │   │   ├── 13450
│       │           │   │   ├── 13451
│       │           │   │   ├── 13451_fsm
│       │           │   │   ├── 13451_vm
│       │           │   │   ├── 13454
│       │           │   │   ├── 13455
│       │           │   │   ├── 1417
│       │           │   │   ├── 1418
│       │           │   │   ├── 16385
│       │           │   │   ├── 16385_fsm
│       │           │   │   ├── 16385_vm
│       │           │   │   ├── 16388
│       │           │   │   ├── 16401
│       │           │   │   ├── 16407
│       │           │   │   ├── 16408
│       │           │   │   ├── 16409
│       │           │   │   ├── 16411
│       │           │   │   ├── 16413
│       │           │   │   ├── 16415
│       │           │   │   ├── 16422
│       │           │   │   ├── 16423
│       │           │   │   ├── 16424
│       │           │   │   ├── 16426
│       │           │   │   ├── 16427
│       │           │   │   ├── 16432
│       │           │   │   ├── 16433
│       │           │   │   ├── 16434
│       │           │   │   ├── 16436
│       │           │   │   ├── 16437
│       │           │   │   ├── 16442
│       │           │   │   ├── 16444
│       │           │   │   ├── 16445
│       │           │   │   ├── 16446
│       │           │   │   ├── 16451
│       │           │   │   ├── 16453
│       │           │   │   ├── 16454
│       │           │   │   ├── 16460
│       │           │   │   ├── 16461
│       │           │   │   ├── 16462
│       │           │   │   ├── 16464
│       │           │   │   ├── 16465
│       │           │   │   ├── 16474
│       │           │   │   ├── 16475
│       │           │   │   ├── 16476
│       │           │   │   ├── 16478
│       │           │   │   ├── 16479
│       │           │   │   ├── 16480
│       │           │   │   ├── 16481
│       │           │   │   ├── 16485
│       │           │   │   ├── 16486
│       │           │   │   ├── 16487
│       │           │   │   ├── 16489
│       │           │   │   ├── 16491
│       │           │   │   ├── 16495
│       │           │   │   ├── 16496
│       │           │   │   ├── 16497
│       │           │   │   ├── 16499
│       │           │   │   ├── 16501
│       │           │   │   ├── 16508
│       │           │   │   ├── 16509
│       │           │   │   ├── 16510
│       │           │   │   ├── 16512
│       │           │   │   ├── 16513
│       │           │   │   ├── 16517
│       │           │   │   ├── 16518
│       │           │   │   ├── 16519
│       │           │   │   ├── 16521
│       │           │   │   ├── 16523
│       │           │   │   ├── 16524
│       │           │   │   ├── 16530
│       │           │   │   ├── 16531
│       │           │   │   ├── 16532
│       │           │   │   ├── 16534
│       │           │   │   ├── 16535
│       │           │   │   ├── 16540
│       │           │   │   ├── 16541
│       │           │   │   ├── 16542
│       │           │   │   ├── 16544
│       │           │   │   ├── 16545
│       │           │   │   ├── 16553
│       │           │   │   ├── 16554
│       │           │   │   ├── 16555
│       │           │   │   ├── 16557
│       │           │   │   ├── 16558
│       │           │   │   ├── 16562
│       │           │   │   ├── 16564
│       │           │   │   ├── 16571
│       │           │   │   ├── 16572
│       │           │   │   ├── 16573
│       │           │   │   ├── 16575
│       │           │   │   ├── 16576
│       │           │   │   ├── 16577
│       │           │   │   ├── 16578
│       │           │   │   ├── 16579
│       │           │   │   ├── 16580
│       │           │   │   ├── 16590
│       │           │   │   ├── 16591
│       │           │   │   ├── 16592
│       │           │   │   ├── 16594
│       │           │   │   ├── 16595
│       │           │   │   ├── 16596
│       │           │   │   ├── 16601
│       │           │   │   ├── 16602
│       │           │   │   ├── 16603
│       │           │   │   ├── 16607
│       │           │   │   ├── 16614
│       │           │   │   ├── 16615
│       │           │   │   ├── 16616
│       │           │   │   ├── 16618
│       │           │   │   ├── 16619
│       │           │   │   ├── 16620
│       │           │   │   ├── 16626
│       │           │   │   ├── 16628
│       │           │   │   ├── 16630
│       │           │   │   ├── 16631
│       │           │   │   ├── 16632
│       │           │   │   ├── 16633
│       │           │   │   ├── 16639
│       │           │   │   ├── 16641
│       │           │   │   ├── 16642
│       │           │   │   ├── 16643
│       │           │   │   ├── 16648
│       │           │   │   ├── 16649
│       │           │   │   ├── 16650
│       │           │   │   ├── 16652
│       │           │   │   ├── 16653
│       │           │   │   ├── 16654
│       │           │   │   ├── 16659
│       │           │   │   ├── 16660
│       │           │   │   ├── 16661
│       │           │   │   ├── 16663
│       │           │   │   ├── 16664
│       │           │   │   ├── 16670
│       │           │   │   ├── 16671
│       │           │   │   ├── 16672
│       │           │   │   ├── 16674
│       │           │   │   ├── 16675
│       │           │   │   ├── 16676
│       │           │   │   ├── 16677
│       │           │   │   ├── 16683
│       │           │   │   ├── 16684
│       │           │   │   ├── 16685
│       │           │   │   ├── 16687
│       │           │   │   ├── 16688
│       │           │   │   ├── 16693
│       │           │   │   ├── 16712
│       │           │   │   ├── 16718
│       │           │   │   ├── 16719
│       │           │   │   ├── 16720
│       │           │   │   ├── 16722
│       │           │   │   ├── 16724
│       │           │   │   ├── 16729
│       │           │   │   ├── 16743
│       │           │   │   ├── 16751
│       │           │   │   ├── 16752
│       │           │   │   ├── 16753
│       │           │   │   ├── 16755
│       │           │   │   ├── 16756
│       │           │   │   ├── 16757
│       │           │   │   ├── 16764
│       │           │   │   ├── 16766
│       │           │   │   ├── 16768
│       │           │   │   ├── 16769
│       │           │   │   ├── 16770
│       │           │   │   ├── 16778
│       │           │   │   ├── 16779
│       │           │   │   ├── 16780
│       │           │   │   ├── 16782
│       │           │   │   ├── 16788
│       │           │   │   ├── 16789
│       │           │   │   ├── 16790
│       │           │   │   ├── 16792
│       │           │   │   ├── 16793
│       │           │   │   ├── 16799
│       │           │   │   ├── 16800
│       │           │   │   ├── 16801
│       │           │   │   ├── 16803
│       │           │   │   ├── 16804
│       │           │   │   ├── 16805
│       │           │   │   ├── 16806
│       │           │   │   ├── 16816
│       │           │   │   ├── 16817
│       │           │   │   ├── 16818
│       │           │   │   ├── 16820
│       │           │   │   ├── 16821
│       │           │   │   ├── 16822
│       │           │   │   ├── 16823
│       │           │   │   ├── 16825
│       │           │   │   ├── 16827
│       │           │   │   ├── 16829
│       │           │   │   ├── 16831
│       │           │   │   ├── 16838
│       │           │   │   ├── 16839
│       │           │   │   ├── 16840
│       │           │   │   ├── 16842
│       │           │   │   ├── 16843
│       │           │   │   ├── 16846
│       │           │   │   ├── 16853
│       │           │   │   ├── 16854
│       │           │   │   ├── 16855
│       │           │   │   ├── 16857
│       │           │   │   ├── 16861
│       │           │   │   ├── 16868
│       │           │   │   ├── 16869
│       │           │   │   ├── 16870
│       │           │   │   ├── 16872
│       │           │   │   ├── 16874
│       │           │   │   ├── 16875
│       │           │   │   ├── 16881
│       │           │   │   ├── 16883
│       │           │   │   ├── 16884
│       │           │   │   ├── 16890
│       │           │   │   ├── 16892
│       │           │   │   ├── 16901
│       │           │   │   ├── 16904
│       │           │   │   ├── 16905
│       │           │   │   ├── 16906
│       │           │   │   ├── 16907
│       │           │   │   ├── 16908
│       │           │   │   ├── 16909
│       │           │   │   ├── 16917
│       │           │   │   ├── 16918
│       │           │   │   ├── 16919
│       │           │   │   ├── 16921
│       │           │   │   ├── 16931
│       │           │   │   ├── 16936
│       │           │   │   ├── 16937
│       │           │   │   ├── 16938
│       │           │   │   ├── 16940
│       │           │   │   ├── 16941
│       │           │   │   ├── 16946
│       │           │   │   ├── 16948
│       │           │   │   ├── 16949
│       │           │   │   ├── 16951
│       │           │   │   ├── 16956
│       │           │   │   ├── 16957
│       │           │   │   ├── 16958
│       │           │   │   ├── 16960
│       │           │   │   ├── 16961
│       │           │   │   ├── 16966
│       │           │   │   ├── 16967
│       │           │   │   ├── 16968
│       │           │   │   ├── 16970
│       │           │   │   ├── 16971
│       │           │   │   ├── 16973
│       │           │   │   ├── 16974
│       │           │   │   ├── 16979
│       │           │   │   ├── 16980
│       │           │   │   ├── 16981
│       │           │   │   ├── 16983
│       │           │   │   ├── 16984
│       │           │   │   ├── 16985
│       │           │   │   ├── 16989
│       │           │   │   ├── 16990
│       │           │   │   ├── 16997
│       │           │   │   ├── 16999
│       │           │   │   ├── 17010
│       │           │   │   ├── 17016
│       │           │   │   ├── 17017
│       │           │   │   ├── 17018
│       │           │   │   ├── 17020
│       │           │   │   ├── 17022
│       │           │   │   ├── 17028
│       │           │   │   ├── 17029
│       │           │   │   ├── 17030
│       │           │   │   ├── 17032
│       │           │   │   ├── 17041
│       │           │   │   ├── 17051
│       │           │   │   ├── 17052
│       │           │   │   ├── 17053
│       │           │   │   ├── 17055
│       │           │   │   ├── 17061
│       │           │   │   ├── 17062
│       │           │   │   ├── 17063
│       │           │   │   ├── 17065
│       │           │   │   ├── 17068
│       │           │   │   ├── 17069
│       │           │   │   ├── 17070
│       │           │   │   ├── 17071
│       │           │   │   ├── 17075
│       │           │   │   ├── 17076
│       │           │   │   ├── 17077
│       │           │   │   ├── 17079
│       │           │   │   ├── 17080
│       │           │   │   ├── 17081
│       │           │   │   ├── 17083
│       │           │   │   ├── 17086
│       │           │   │   ├── 17087
│       │           │   │   ├── 17090
│       │           │   │   ├── 17092
│       │           │   │   ├── 17097
│       │           │   │   ├── 17098
│       │           │   │   ├── 17099
│       │           │   │   ├── 17101
│       │           │   │   ├── 17102
│       │           │   │   ├── 17108
│       │           │   │   ├── 17109
│       │           │   │   ├── 17110
│       │           │   │   ├── 17112
│       │           │   │   ├── 17113
│       │           │   │   ├── 17114
│       │           │   │   ├── 17122
│       │           │   │   ├── 17123
│       │           │   │   ├── 17124
│       │           │   │   ├── 17126
│       │           │   │   ├── 17127
│       │           │   │   ├── 17132
│       │           │   │   ├── 17133
│       │           │   │   ├── 17134
│       │           │   │   ├── 17136
│       │           │   │   ├── 17142
│       │           │   │   ├── 17147
│       │           │   │   ├── 17149
│       │           │   │   ├── 17150
│       │           │   │   ├── 17151
│       │           │   │   ├── 17156
│       │           │   │   ├── 17158
│       │           │   │   ├── 17159
│       │           │   │   ├── 174
│       │           │   │   ├── 175
│       │           │   │   ├── 2187
│       │           │   │   ├── 2224
│       │           │   │   ├── 2228
│       │           │   │   ├── 2328
│       │           │   │   ├── 2336
│       │           │   │   ├── 2337
│       │           │   │   ├── 2579
│       │           │   │   ├── 2600
│       │           │   │   ├── 2600_fsm
│       │           │   │   ├── 2600_vm
│       │           │   │   ├── 2601
│       │           │   │   ├── 2601_fsm
│       │           │   │   ├── 2601_vm
│       │           │   │   ├── 2602
│       │           │   │   ├── 2602_fsm
│       │           │   │   ├── 2602_vm
│       │           │   │   ├── 2603
│       │           │   │   ├── 2603_fsm
│       │           │   │   ├── 2603_vm
│       │           │   │   ├── 2604
│       │           │   │   ├── 2604_fsm
│       │           │   │   ├── 2605
│       │           │   │   ├── 2605_fsm
│       │           │   │   ├── 2605_vm
│       │           │   │   ├── 2606
│       │           │   │   ├── 2606_fsm
│       │           │   │   ├── 2606_vm
│       │           │   │   ├── 2607
│       │           │   │   ├── 2607_fsm
│       │           │   │   ├── 2607_vm
│       │           │   │   ├── 2608
│       │           │   │   ├── 2608_fsm
│       │           │   │   ├── 2608_vm
│       │           │   │   ├── 2609
│       │           │   │   ├── 2609_fsm
│       │           │   │   ├── 2609_vm
│       │           │   │   ├── 2610
│       │           │   │   ├── 2610_fsm
│       │           │   │   ├── 2610_vm
│       │           │   │   ├── 2611
│       │           │   │   ├── 2612
│       │           │   │   ├── 2612_fsm
│       │           │   │   ├── 2612_vm
│       │           │   │   ├── 2613
│       │           │   │   ├── 2615
│       │           │   │   ├── 2615_fsm
│       │           │   │   ├── 2615_vm
│       │           │   │   ├── 2616
│       │           │   │   ├── 2616_fsm
│       │           │   │   ├── 2616_vm
│       │           │   │   ├── 2617
│       │           │   │   ├── 2617_fsm
│       │           │   │   ├── 2617_vm
│       │           │   │   ├── 2618
│       │           │   │   ├── 2618_fsm
│       │           │   │   ├── 2618_vm
│       │           │   │   ├── 2619
│       │           │   │   ├── 2619_fsm
│       │           │   │   ├── 2619_vm
│       │           │   │   ├── 2620
│       │           │   │   ├── 2650
│       │           │   │   ├── 2651
│       │           │   │   ├── 2652
│       │           │   │   ├── 2653
│       │           │   │   ├── 2654
│       │           │   │   ├── 2655
│       │           │   │   ├── 2656
│       │           │   │   ├── 2657
│       │           │   │   ├── 2658
│       │           │   │   ├── 2659
│       │           │   │   ├── 2660
│       │           │   │   ├── 2661
│       │           │   │   ├── 2662
│       │           │   │   ├── 2663
│       │           │   │   ├── 2664
│       │           │   │   ├── 2665
│       │           │   │   ├── 2666
│       │           │   │   ├── 2667
│       │           │   │   ├── 2668
│       │           │   │   ├── 2669
│       │           │   │   ├── 2670
│       │           │   │   ├── 2673
│       │           │   │   ├── 2674
│       │           │   │   ├── 2675
│       │           │   │   ├── 2678
│       │           │   │   ├── 2679
│       │           │   │   ├── 2680
│       │           │   │   ├── 2681
│       │           │   │   ├── 2682
│       │           │   │   ├── 2683
│       │           │   │   ├── 2684
│       │           │   │   ├── 2685
│       │           │   │   ├── 2686
│       │           │   │   ├── 2687
│       │           │   │   ├── 2688
│       │           │   │   ├── 2689
│       │           │   │   ├── 2690
│       │           │   │   ├── 2691
│       │           │   │   ├── 2692
│       │           │   │   ├── 2693
│       │           │   │   ├── 2696
│       │           │   │   ├── 2699
│       │           │   │   ├── 2701
│       │           │   │   ├── 2702
│       │           │   │   ├── 2703
│       │           │   │   ├── 2704
│       │           │   │   ├── 2753
│       │           │   │   ├── 2753_fsm
│       │           │   │   ├── 2753_vm
│       │           │   │   ├── 2754
│       │           │   │   ├── 2755
│       │           │   │   ├── 2756
│       │           │   │   ├── 2757
│       │           │   │   ├── 2830
│       │           │   │   ├── 2831
│       │           │   │   ├── 2832
│       │           │   │   ├── 2833
│       │           │   │   ├── 2834
│       │           │   │   ├── 2835
│       │           │   │   ├── 2836
│       │           │   │   ├── 2836_fsm
│       │           │   │   ├── 2836_vm
│       │           │   │   ├── 2837
│       │           │   │   ├── 2838
│       │           │   │   ├── 2838_fsm
│       │           │   │   ├── 2838_vm
│       │           │   │   ├── 2839
│       │           │   │   ├── 2840
│       │           │   │   ├── 2840_fsm
│       │           │   │   ├── 2840_vm
│       │           │   │   ├── 2841
│       │           │   │   ├── 2995
│       │           │   │   ├── 2996
│       │           │   │   ├── 3079
│       │           │   │   ├── 3079_fsm
│       │           │   │   ├── 3079_vm
│       │           │   │   ├── 3080
│       │           │   │   ├── 3081
│       │           │   │   ├── 3085
│       │           │   │   ├── 3118
│       │           │   │   ├── 3119
│       │           │   │   ├── 3164
│       │           │   │   ├── 3256
│       │           │   │   ├── 3257
│       │           │   │   ├── 3258
│       │           │   │   ├── 3350
│       │           │   │   ├── 3351
│       │           │   │   ├── 3379
│       │           │   │   ├── 3380
│       │           │   │   ├── 3381
│       │           │   │   ├── 3394
│       │           │   │   ├── 3394_fsm
│       │           │   │   ├── 3394_vm
│       │           │   │   ├── 3395
│       │           │   │   ├── 3429
│       │           │   │   ├── 3430
│       │           │   │   ├── 3431
│       │           │   │   ├── 3433
│       │           │   │   ├── 3439
│       │           │   │   ├── 3440
│       │           │   │   ├── 3455
│       │           │   │   ├── 3456
│       │           │   │   ├── 3456_fsm
│       │           │   │   ├── 3456_vm
│       │           │   │   ├── 3466
│       │           │   │   ├── 3467
│       │           │   │   ├── 3468
│       │           │   │   ├── 3501
│       │           │   │   ├── 3502
│       │           │   │   ├── 3503
│       │           │   │   ├── 3534
│       │           │   │   ├── 3541
│       │           │   │   ├── 3541_fsm
│       │           │   │   ├── 3541_vm
│       │           │   │   ├── 3542
│       │           │   │   ├── 3574
│       │           │   │   ├── 3575
│       │           │   │   ├── 3576
│       │           │   │   ├── 3596
│       │           │   │   ├── 3597
│       │           │   │   ├── 3598
│       │           │   │   ├── 3599
│       │           │   │   ├── 3600
│       │           │   │   ├── 3600_fsm
│       │           │   │   ├── 3600_vm
│       │           │   │   ├── 3601
│       │           │   │   ├── 3601_fsm
│       │           │   │   ├── 3601_vm
│       │           │   │   ├── 3602
│       │           │   │   ├── 3602_fsm
│       │           │   │   ├── 3602_vm
│       │           │   │   ├── 3603
│       │           │   │   ├── 3603_fsm
│       │           │   │   ├── 3603_vm
│       │           │   │   ├── 3604
│       │           │   │   ├── 3605
│       │           │   │   ├── 3606
│       │           │   │   ├── 3607
│       │           │   │   ├── 3608
│       │           │   │   ├── 3609
│       │           │   │   ├── 3712
│       │           │   │   ├── 3764
│       │           │   │   ├── 3764_fsm
│       │           │   │   ├── 3764_vm
│       │           │   │   ├── 3766
│       │           │   │   ├── 3767
│       │           │   │   ├── 3997
│       │           │   │   ├── 4143
│       │           │   │   ├── 4144
│       │           │   │   ├── 4145
│       │           │   │   ├── 4146
│       │           │   │   ├── 4147
│       │           │   │   ├── 4148
│       │           │   │   ├── 4149
│       │           │   │   ├── 4150
│       │           │   │   ├── 4151
│       │           │   │   ├── 4152
│       │           │   │   ├── 4153
│       │           │   │   ├── 4154
│       │           │   │   ├── 4155
│       │           │   │   ├── 4156
│       │           │   │   ├── 4157
│       │           │   │   ├── 4158
│       │           │   │   ├── 4159
│       │           │   │   ├── 4160
│       │           │   │   ├── 4163
│       │           │   │   ├── 4164
│       │           │   │   ├── 4165
│       │           │   │   ├── 4166
│       │           │   │   ├── 4167
│       │           │   │   ├── 4168
│       │           │   │   ├── 4169
│       │           │   │   ├── 4170
│       │           │   │   ├── 4171
│       │           │   │   ├── 4172
│       │           │   │   ├── 4173
│       │           │   │   ├── 4174
│       │           │   │   ├── 5002
│       │           │   │   ├── 548
│       │           │   │   ├── 549
│       │           │   │   ├── 6102
│       │           │   │   ├── 6104
│       │           │   │   ├── 6106
│       │           │   │   ├── 6110
│       │           │   │   ├── 6111
│       │           │   │   ├── 6112
│       │           │   │   ├── 6113
│       │           │   │   ├── 6116
│       │           │   │   ├── 6117
│       │           │   │   ├── 6175
│       │           │   │   ├── 6176
│       │           │   │   ├── 6228
│       │           │   │   ├── 6229
│       │           │   │   ├── 6237
│       │           │   │   ├── 6238
│       │           │   │   ├── 6239
│       │           │   │   ├── 826
│       │           │   │   ├── 827
│       │           │   │   ├── 828
│       │           │   │   ├── PG_VERSION
│       │           │   │   ├── pg_filenode.map
│       │           │   │   └── pg_internal.init
│       │           │   ├── 4
│       │           │   │   ├── 112
│       │           │   │   ├── 113
│       │           │   │   ├── 1247
│       │           │   │   ├── 1247_fsm
│       │           │   │   ├── 1247_vm
│       │           │   │   ├── 1249
│       │           │   │   ├── 1249_fsm
│       │           │   │   ├── 1249_vm
│       │           │   │   ├── 1255
│       │           │   │   ├── 1255_fsm
│       │           │   │   ├── 1255_vm
│       │           │   │   ├── 1259
│       │           │   │   ├── 1259_fsm
│       │           │   │   ├── 1259_vm
│       │           │   │   ├── 13436
│       │           │   │   ├── 13436_fsm
│       │           │   │   ├── 13436_vm
│       │           │   │   ├── 13439
│       │           │   │   ├── 13440
│       │           │   │   ├── 13441
│       │           │   │   ├── 13441_fsm
│       │           │   │   ├── 13441_vm
│       │           │   │   ├── 13444
│       │           │   │   ├── 13445
│       │           │   │   ├── 13446
│       │           │   │   ├── 13446_fsm
│       │           │   │   ├── 13446_vm
│       │           │   │   ├── 13449
│       │           │   │   ├── 13450
│       │           │   │   ├── 13451
│       │           │   │   ├── 13451_fsm
│       │           │   │   ├── 13451_vm
│       │           │   │   ├── 13454
│       │           │   │   ├── 13455
│       │           │   │   ├── 1417
│       │           │   │   ├── 1418
│       │           │   │   ├── 174
│       │           │   │   ├── 175
│       │           │   │   ├── 2187
│       │           │   │   ├── 2224
│       │           │   │   ├── 2228
│       │           │   │   ├── 2328
│       │           │   │   ├── 2336
│       │           │   │   ├── 2337
│       │           │   │   ├── 2579
│       │           │   │   ├── 2600
│       │           │   │   ├── 2600_fsm
│       │           │   │   ├── 2600_vm
│       │           │   │   ├── 2601
│       │           │   │   ├── 2601_fsm
│       │           │   │   ├── 2601_vm
│       │           │   │   ├── 2602
│       │           │   │   ├── 2602_fsm
│       │           │   │   ├── 2602_vm
│       │           │   │   ├── 2603
│       │           │   │   ├── 2603_fsm
│       │           │   │   ├── 2603_vm
│       │           │   │   ├── 2604
│       │           │   │   ├── 2605
│       │           │   │   ├── 2605_fsm
│       │           │   │   ├── 2605_vm
│       │           │   │   ├── 2606
│       │           │   │   ├── 2606_fsm
│       │           │   │   ├── 2606_vm
│       │           │   │   ├── 2607
│       │           │   │   ├── 2607_fsm
│       │           │   │   ├── 2607_vm
│       │           │   │   ├── 2608
│       │           │   │   ├── 2608_fsm
│       │           │   │   ├── 2608_vm
│       │           │   │   ├── 2609
│       │           │   │   ├── 2609_fsm
│       │           │   │   ├── 2609_vm
│       │           │   │   ├── 2610
│       │           │   │   ├── 2610_fsm
│       │           │   │   ├── 2610_vm
│       │           │   │   ├── 2611
│       │           │   │   ├── 2612
│       │           │   │   ├── 2612_fsm
│       │           │   │   ├── 2612_vm
│       │           │   │   ├── 2613
│       │           │   │   ├── 2615
│       │           │   │   ├── 2615_fsm
│       │           │   │   ├── 2615_vm
│       │           │   │   ├── 2616
│       │           │   │   ├── 2616_fsm
│       │           │   │   ├── 2616_vm
│       │           │   │   ├── 2617
│       │           │   │   ├── 2617_fsm
│       │           │   │   ├── 2617_vm
│       │           │   │   ├── 2618
│       │           │   │   ├── 2618_fsm
│       │           │   │   ├── 2618_vm
│       │           │   │   ├── 2619
│       │           │   │   ├── 2619_fsm
│       │           │   │   ├── 2619_vm
│       │           │   │   ├── 2620
│       │           │   │   ├── 2650
│       │           │   │   ├── 2651
│       │           │   │   ├── 2652
│       │           │   │   ├── 2653
│       │           │   │   ├── 2654
│       │           │   │   ├── 2655
│       │           │   │   ├── 2656
│       │           │   │   ├── 2657
│       │           │   │   ├── 2658
│       │           │   │   ├── 2659
│       │           │   │   ├── 2660
│       │           │   │   ├── 2661
│       │           │   │   ├── 2662
│       │           │   │   ├── 2663
│       │           │   │   ├── 2664
│       │           │   │   ├── 2665
│       │           │   │   ├── 2666
│       │           │   │   ├── 2667
│       │           │   │   ├── 2668
│       │           │   │   ├── 2669
│       │           │   │   ├── 2670
│       │           │   │   ├── 2673
│       │           │   │   ├── 2674
│       │           │   │   ├── 2675
│       │           │   │   ├── 2678
│       │           │   │   ├── 2679
│       │           │   │   ├── 2680
│       │           │   │   ├── 2681
│       │           │   │   ├── 2682
│       │           │   │   ├── 2683
│       │           │   │   ├── 2684
│       │           │   │   ├── 2685
│       │           │   │   ├── 2686
│       │           │   │   ├── 2687
│       │           │   │   ├── 2688
│       │           │   │   ├── 2689
│       │           │   │   ├── 2690
│       │           │   │   ├── 2691
│       │           │   │   ├── 2692
│       │           │   │   ├── 2693
│       │           │   │   ├── 2696
│       │           │   │   ├── 2699
│       │           │   │   ├── 2701
│       │           │   │   ├── 2702
│       │           │   │   ├── 2703
│       │           │   │   ├── 2704
│       │           │   │   ├── 2753
│       │           │   │   ├── 2753_fsm
│       │           │   │   ├── 2753_vm
│       │           │   │   ├── 2754
│       │           │   │   ├── 2755
│       │           │   │   ├── 2756
│       │           │   │   ├── 2757
│       │           │   │   ├── 2830
│       │           │   │   ├── 2831
│       │           │   │   ├── 2832
│       │           │   │   ├── 2833
│       │           │   │   ├── 2834
│       │           │   │   ├── 2835
│       │           │   │   ├── 2836
│       │           │   │   ├── 2836_fsm
│       │           │   │   ├── 2836_vm
│       │           │   │   ├── 2837
│       │           │   │   ├── 2838
│       │           │   │   ├── 2838_fsm
│       │           │   │   ├── 2838_vm
│       │           │   │   ├── 2839
│       │           │   │   ├── 2840
│       │           │   │   ├── 2840_fsm
│       │           │   │   ├── 2840_vm
│       │           │   │   ├── 2841
│       │           │   │   ├── 2995
│       │           │   │   ├── 2996
│       │           │   │   ├── 3079
│       │           │   │   ├── 3079_fsm
│       │           │   │   ├── 3079_vm
│       │           │   │   ├── 3080
│       │           │   │   ├── 3081
│       │           │   │   ├── 3085
│       │           │   │   ├── 3118
│       │           │   │   ├── 3119
│       │           │   │   ├── 3164
│       │           │   │   ├── 3256
│       │           │   │   ├── 3257
│       │           │   │   ├── 3258
│       │           │   │   ├── 3350
│       │           │   │   ├── 3351
│       │           │   │   ├── 3379
│       │           │   │   ├── 3380
│       │           │   │   ├── 3381
│       │           │   │   ├── 3394
│       │           │   │   ├── 3394_fsm
│       │           │   │   ├── 3394_vm
│       │           │   │   ├── 3395
│       │           │   │   ├── 3429
│       │           │   │   ├── 3430
│       │           │   │   ├── 3431
│       │           │   │   ├── 3433
│       │           │   │   ├── 3439
│       │           │   │   ├── 3440
│       │           │   │   ├── 3455
│       │           │   │   ├── 3456
│       │           │   │   ├── 3456_fsm
│       │           │   │   ├── 3456_vm
│       │           │   │   ├── 3466
│       │           │   │   ├── 3467
│       │           │   │   ├── 3468
│       │           │   │   ├── 3501
│       │           │   │   ├── 3502
│       │           │   │   ├── 3503
│       │           │   │   ├── 3534
│       │           │   │   ├── 3541
│       │           │   │   ├── 3541_fsm
│       │           │   │   ├── 3541_vm
│       │           │   │   ├── 3542
│       │           │   │   ├── 3574
│       │           │   │   ├── 3575
│       │           │   │   ├── 3576
│       │           │   │   ├── 3596
│       │           │   │   ├── 3597
│       │           │   │   ├── 3598
│       │           │   │   ├── 3599
│       │           │   │   ├── 3600
│       │           │   │   ├── 3600_fsm
│       │           │   │   ├── 3600_vm
│       │           │   │   ├── 3601
│       │           │   │   ├── 3601_fsm
│       │           │   │   ├── 3601_vm
│       │           │   │   ├── 3602
│       │           │   │   ├── 3602_fsm
│       │           │   │   ├── 3602_vm
│       │           │   │   ├── 3603
│       │           │   │   ├── 3603_fsm
│       │           │   │   ├── 3603_vm
│       │           │   │   ├── 3604
│       │           │   │   ├── 3605
│       │           │   │   ├── 3606
│       │           │   │   ├── 3607
│       │           │   │   ├── 3608
│       │           │   │   ├── 3609
│       │           │   │   ├── 3712
│       │           │   │   ├── 3764
│       │           │   │   ├── 3764_fsm
│       │           │   │   ├── 3764_vm
│       │           │   │   ├── 3766
│       │           │   │   ├── 3767
│       │           │   │   ├── 3997
│       │           │   │   ├── 4143
│       │           │   │   ├── 4144
│       │           │   │   ├── 4145
│       │           │   │   ├── 4146
│       │           │   │   ├── 4147
│       │           │   │   ├── 4148
│       │           │   │   ├── 4149
│       │           │   │   ├── 4150
│       │           │   │   ├── 4151
│       │           │   │   ├── 4152
│       │           │   │   ├── 4153
│       │           │   │   ├── 4154
│       │           │   │   ├── 4155
│       │           │   │   ├── 4156
│       │           │   │   ├── 4157
│       │           │   │   ├── 4158
│       │           │   │   ├── 4159
│       │           │   │   ├── 4160
│       │           │   │   ├── 4163
│       │           │   │   ├── 4164
│       │           │   │   ├── 4165
│       │           │   │   ├── 4166
│       │           │   │   ├── 4167
│       │           │   │   ├── 4168
│       │           │   │   ├── 4169
│       │           │   │   ├── 4170
│       │           │   │   ├── 4171
│       │           │   │   ├── 4172
│       │           │   │   ├── 4173
│       │           │   │   ├── 4174
│       │           │   │   ├── 5002
│       │           │   │   ├── 548
│       │           │   │   ├── 549
│       │           │   │   ├── 6102
│       │           │   │   ├── 6104
│       │           │   │   ├── 6106
│       │           │   │   ├── 6110
│       │           │   │   ├── 6111
│       │           │   │   ├── 6112
│       │           │   │   ├── 6113
│       │           │   │   ├── 6116
│       │           │   │   ├── 6117
│       │           │   │   ├── 6175
│       │           │   │   ├── 6176
│       │           │   │   ├── 6228
│       │           │   │   ├── 6229
│       │           │   │   ├── 6237
│       │           │   │   ├── 6238
│       │           │   │   ├── 6239
│       │           │   │   ├── 826
│       │           │   │   ├── 827
│       │           │   │   ├── 828
│       │           │   │   ├── PG_VERSION
│       │           │   │   └── pg_filenode.map
│       │           │   └── 5
│       │           │       ├── 112
│       │           │       ├── 113
│       │           │       ├── 1247
│       │           │       ├── 1247_fsm
│       │           │       ├── 1247_vm
│       │           │       ├── 1249
│       │           │       ├── 1249_fsm
│       │           │       ├── 1249_vm
│       │           │       ├── 1255
│       │           │       ├── 1255_fsm
│       │           │       ├── 1255_vm
│       │           │       ├── 1259
│       │           │       ├── 1259_fsm
│       │           │       ├── 1259_vm
│       │           │       ├── 13436
│       │           │       ├── 13436_fsm
│       │           │       ├── 13436_vm
│       │           │       ├── 13439
│       │           │       ├── 13440
│       │           │       ├── 13441
│       │           │       ├── 13441_fsm
│       │           │       ├── 13441_vm
│       │           │       ├── 13444
│       │           │       ├── 13445
│       │           │       ├── 13446
│       │           │       ├── 13446_fsm
│       │           │       ├── 13446_vm
│       │           │       ├── 13449
│       │           │       ├── 13450
│       │           │       ├── 13451
│       │           │       ├── 13451_fsm
│       │           │       ├── 13451_vm
│       │           │       ├── 13454
│       │           │       ├── 13455
│       │           │       ├── 1417
│       │           │       ├── 1418
│       │           │       ├── 174
│       │           │       ├── 175
│       │           │       ├── 2187
│       │           │       ├── 2224
│       │           │       ├── 2228
│       │           │       ├── 2328
│       │           │       ├── 2336
│       │           │       ├── 2337
│       │           │       ├── 2579
│       │           │       ├── 2600
│       │           │       ├── 2600_fsm
│       │           │       ├── 2600_vm
│       │           │       ├── 2601
│       │           │       ├── 2601_fsm
│       │           │       ├── 2601_vm
│       │           │       ├── 2602
│       │           │       ├── 2602_fsm
│       │           │       ├── 2602_vm
│       │           │       ├── 2603
│       │           │       ├── 2603_fsm
│       │           │       ├── 2603_vm
│       │           │       ├── 2604
│       │           │       ├── 2605
│       │           │       ├── 2605_fsm
│       │           │       ├── 2605_vm
│       │           │       ├── 2606
│       │           │       ├── 2606_fsm
│       │           │       ├── 2606_vm
│       │           │       ├── 2607
│       │           │       ├── 2607_fsm
│       │           │       ├── 2607_vm
│       │           │       ├── 2608
│       │           │       ├── 2608_fsm
│       │           │       ├── 2608_vm
│       │           │       ├── 2609
│       │           │       ├── 2609_fsm
│       │           │       ├── 2609_vm
│       │           │       ├── 2610
│       │           │       ├── 2610_fsm
│       │           │       ├── 2610_vm
│       │           │       ├── 2611
│       │           │       ├── 2612
│       │           │       ├── 2612_fsm
│       │           │       ├── 2612_vm
│       │           │       ├── 2613
│       │           │       ├── 2615
│       │           │       ├── 2615_fsm
│       │           │       ├── 2615_vm
│       │           │       ├── 2616
│       │           │       ├── 2616_fsm
│       │           │       ├── 2616_vm
│       │           │       ├── 2617
│       │           │       ├── 2617_fsm
│       │           │       ├── 2617_vm
│       │           │       ├── 2618
│       │           │       ├── 2618_fsm
│       │           │       ├── 2618_vm
│       │           │       ├── 2619
│       │           │       ├── 2619_fsm
│       │           │       ├── 2619_vm
│       │           │       ├── 2620
│       │           │       ├── 2650
│       │           │       ├── 2651
│       │           │       ├── 2652
│       │           │       ├── 2653
│       │           │       ├── 2654
│       │           │       ├── 2655
│       │           │       ├── 2656
│       │           │       ├── 2657
│       │           │       ├── 2658
│       │           │       ├── 2659
│       │           │       ├── 2660
│       │           │       ├── 2661
│       │           │       ├── 2662
│       │           │       ├── 2663
│       │           │       ├── 2664
│       │           │       ├── 2665
│       │           │       ├── 2666
│       │           │       ├── 2667
│       │           │       ├── 2668
│       │           │       ├── 2669
│       │           │       ├── 2670
│       │           │       ├── 2673
│       │           │       ├── 2674
│       │           │       ├── 2675
│       │           │       ├── 2678
│       │           │       ├── 2679
│       │           │       ├── 2680
│       │           │       ├── 2681
│       │           │       ├── 2682
│       │           │       ├── 2683
│       │           │       ├── 2684
│       │           │       ├── 2685
│       │           │       ├── 2686
│       │           │       ├── 2687
│       │           │       ├── 2688
│       │           │       ├── 2689
│       │           │       ├── 2690
│       │           │       ├── 2691
│       │           │       ├── 2692
│       │           │       ├── 2693
│       │           │       ├── 2696
│       │           │       ├── 2699
│       │           │       ├── 2701
│       │           │       ├── 2702
│       │           │       ├── 2703
│       │           │       ├── 2704
│       │           │       ├── 2753
│       │           │       ├── 2753_fsm
│       │           │       ├── 2753_vm
│       │           │       ├── 2754
│       │           │       ├── 2755
│       │           │       ├── 2756
│       │           │       ├── 2757
│       │           │       ├── 2830
│       │           │       ├── 2831
│       │           │       ├── 2832
│       │           │       ├── 2833
│       │           │       ├── 2834
│       │           │       ├── 2835
│       │           │       ├── 2836
│       │           │       ├── 2836_fsm
│       │           │       ├── 2836_vm
│       │           │       ├── 2837
│       │           │       ├── 2838
│       │           │       ├── 2838_fsm
│       │           │       ├── 2838_vm
│       │           │       ├── 2839
│       │           │       ├── 2840
│       │           │       ├── 2840_fsm
│       │           │       ├── 2840_vm
│       │           │       ├── 2841
│       │           │       ├── 2995
│       │           │       ├── 2996
│       │           │       ├── 3079
│       │           │       ├── 3079_fsm
│       │           │       ├── 3079_vm
│       │           │       ├── 3080
│       │           │       ├── 3081
│       │           │       ├── 3085
│       │           │       ├── 3118
│       │           │       ├── 3119
│       │           │       ├── 3164
│       │           │       ├── 3256
│       │           │       ├── 3257
│       │           │       ├── 3258
│       │           │       ├── 3350
│       │           │       ├── 3351
│       │           │       ├── 3379
│       │           │       ├── 3380
│       │           │       ├── 3381
│       │           │       ├── 3394
│       │           │       ├── 3394_fsm
│       │           │       ├── 3394_vm
│       │           │       ├── 3395
│       │           │       ├── 3429
│       │           │       ├── 3430
│       │           │       ├── 3431
│       │           │       ├── 3433
│       │           │       ├── 3439
│       │           │       ├── 3440
│       │           │       ├── 3455
│       │           │       ├── 3456
│       │           │       ├── 3456_fsm
│       │           │       ├── 3456_vm
│       │           │       ├── 3466
│       │           │       ├── 3467
│       │           │       ├── 3468
│       │           │       ├── 3501
│       │           │       ├── 3502
│       │           │       ├── 3503
│       │           │       ├── 3534
│       │           │       ├── 3541
│       │           │       ├── 3541_fsm
│       │           │       ├── 3541_vm
│       │           │       ├── 3542
│       │           │       ├── 3574
│       │           │       ├── 3575
│       │           │       ├── 3576
│       │           │       ├── 3596
│       │           │       ├── 3597
│       │           │       ├── 3598
│       │           │       ├── 3599
│       │           │       ├── 3600
│       │           │       ├── 3600_fsm
│       │           │       ├── 3600_vm
│       │           │       ├── 3601
│       │           │       ├── 3601_fsm
│       │           │       ├── 3601_vm
│       │           │       ├── 3602
│       │           │       ├── 3602_fsm
│       │           │       ├── 3602_vm
│       │           │       ├── 3603
│       │           │       ├── 3603_fsm
│       │           │       ├── 3603_vm
│       │           │       ├── 3604
│       │           │       ├── 3605
│       │           │       ├── 3606
│       │           │       ├── 3607
│       │           │       ├── 3608
│       │           │       ├── 3609
│       │           │       ├── 3712
│       │           │       ├── 3764
│       │           │       ├── 3764_fsm
│       │           │       ├── 3764_vm
│       │           │       ├── 3766
│       │           │       ├── 3767
│       │           │       ├── 3997
│       │           │       ├── 4143
│       │           │       ├── 4144
│       │           │       ├── 4145
│       │           │       ├── 4146
│       │           │       ├── 4147
│       │           │       ├── 4148
│       │           │       ├── 4149
│       │           │       ├── 4150
│       │           │       ├── 4151
│       │           │       ├── 4152
│       │           │       ├── 4153
│       │           │       ├── 4154
│       │           │       ├── 4155
│       │           │       ├── 4156
│       │           │       ├── 4157
│       │           │       ├── 4158
│       │           │       ├── 4159
│       │           │       ├── 4160
│       │           │       ├── 4163
│       │           │       ├── 4164
│       │           │       ├── 4165
│       │           │       ├── 4166
│       │           │       ├── 4167
│       │           │       ├── 4168
│       │           │       ├── 4169
│       │           │       ├── 4170
│       │           │       ├── 4171
│       │           │       ├── 4172
│       │           │       ├── 4173
│       │           │       ├── 4174
│       │           │       ├── 5002
│       │           │       ├── 548
│       │           │       ├── 549
│       │           │       ├── 6102
│       │           │       ├── 6104
│       │           │       ├── 6106
│       │           │       ├── 6110
│       │           │       ├── 6111
│       │           │       ├── 6112
│       │           │       ├── 6113
│       │           │       ├── 6116
│       │           │       ├── 6117
│       │           │       ├── 6175
│       │           │       ├── 6176
│       │           │       ├── 6228
│       │           │       ├── 6229
│       │           │       ├── 6237
│       │           │       ├── 6238
│       │           │       ├── 6239
│       │           │       ├── 826
│       │           │       ├── 827
│       │           │       ├── 828
│       │           │       ├── PG_VERSION
│       │           │       ├── pg_filenode.map
│       │           │       └── pg_internal.init
│       │           ├── global
│       │           │   ├── 1213
│       │           │   ├── 1213_fsm
│       │           │   ├── 1213_vm
│       │           │   ├── 1214
│       │           │   ├── 1232
│       │           │   ├── 1233
│       │           │   ├── 1260
│       │           │   ├── 1260_fsm
│       │           │   ├── 1260_vm
│       │           │   ├── 1261
│       │           │   ├── 1261_fsm
│       │           │   ├── 1261_vm
│       │           │   ├── 1262
│       │           │   ├── 1262_fsm
│       │           │   ├── 1262_vm
│       │           │   ├── 2396
│       │           │   ├── 2396_fsm
│       │           │   ├── 2396_vm
│       │           │   ├── 2397
│       │           │   ├── 2671
│       │           │   ├── 2672
│       │           │   ├── 2676
│       │           │   ├── 2677
│       │           │   ├── 2694
│       │           │   ├── 2695
│       │           │   ├── 2697
│       │           │   ├── 2698
│       │           │   ├── 2846
│       │           │   ├── 2847
│       │           │   ├── 2964
│       │           │   ├── 2965
│       │           │   ├── 2966
│       │           │   ├── 2967
│       │           │   ├── 3592
│       │           │   ├── 3593
│       │           │   ├── 4060
│       │           │   ├── 4061
│       │           │   ├── 4175
│       │           │   ├── 4176
│       │           │   ├── 4177
│       │           │   ├── 4178
│       │           │   ├── 4181
│       │           │   ├── 4182
│       │           │   ├── 4183
│       │           │   ├── 4184
│       │           │   ├── 4185
│       │           │   ├── 4186
│       │           │   ├── 6000
│       │           │   ├── 6001
│       │           │   ├── 6002
│       │           │   ├── 6100
│       │           │   ├── 6114
│       │           │   ├── 6115
│       │           │   ├── 6243
│       │           │   ├── 6244
│       │           │   ├── 6245
│       │           │   ├── 6246
│       │           │   ├── 6247
│       │           │   ├── pg_control
│       │           │   ├── pg_filenode.map
│       │           │   └── pg_internal.init
│       │           ├── pg_commit_ts
│       │           ├── pg_dynshmem
│       │           ├── pg_hba.conf
│       │           ├── pg_ident.conf
│       │           ├── pg_logical
│       │           │   ├── mappings
│       │           │   ├── replorigin_checkpoint
│       │           │   └── snapshots
│       │           ├── pg_multixact
│       │           │   ├── members
│       │           │   │   └── 0000
│       │           │   └── offsets
│       │           │       └── 0000
│       │           ├── pg_notify
│       │           ├── pg_replslot
│       │           ├── pg_serial
│       │           ├── pg_snapshots
│       │           ├── pg_stat
│       │           ├── pg_stat_tmp
│       │           ├── pg_subtrans
│       │           │   └── 0000
│       │           ├── pg_tblspc
│       │           ├── pg_twophase
│       │           ├── pg_wal
│       │           │   ├── 000000010000000000000001
│       │           │   └── archive_status
│       │           ├── pg_xact
│       │           │   └── 0000
│       │           ├── postgresql.auto.conf
│       │           ├── postgresql.conf
│       │           ├── postmaster.opts
│       │           └── postmaster.pid
│       ├── redis
│       │   └── data
│       │       └── dump.rdb
│       ├── sandbox
│       │   └── dependencies
│       │       └── python-requirements.txt
│       ├── ssrf_proxy
│       │   └── squid.conf
│       └── weaviate
│           ├── classifications.db
│           ├── migration1.19.filter2search.skip.flag
│           ├── migration1.19.filter2search.state
│           ├── modules.db
│           └── schema.db
├── docs
│   ├── communication.md
│   ├── execution.md
│   ├── knowledge_graph.md
│   ├── ontology_api.md
│   ├── planning.md
│   └── reasoning.md
├── folder_structure.md
├── images
│   ├── GitHub_README_cover.png
│   ├── demo.png
│   ├── models.png
│   └── wechat.png
├── mabos
│   ├── agents
│   │   ├── __init__.py
│   │   ├── agent.py
│   │   ├── coordinator_agents
│   │   │   ├── business_process_manager.py
│   │   │   └── goal_model_agent.py
│   │   ├── information_agents
│   │   │   ├── data_management_agent.py
│   │   │   └── ontology_agent.py
│   │   ├── interface_agents
│   │   │   └── onboarding_agent.py
│   │   ├── supervisor_agents
│   │   │   ├── enterprise_architecture_agent.py
│   │   │   └── security_agent.py
│   │   ├── task_agents
│   │   │   ├── business_plan_agent.py
│   │   │   └── reporting_agent.py
│   │   └── worker_agents
│   ├── bdi
│   │   ├── __init__.py
│   │   ├── belief.py
│   │   ├── desire.py
│   │   └── intention.py
│   ├── communication
│   │   ├── __init__.py
│   │   ├── broker.py
│   │   ├── communication.py
│   │   ├── communication_ontology.py
│   │   ├── delayed_message_queue.py
│   │   ├── group_formation.py
│   │   ├── message.py
│   │   ├── message_encryptor.py
│   │   ├── message_serializer.py
│   │   ├── message_storage.py
│   │   └── negotiation
│   │       ├── auction_based_negotiation.py
│   │       └── contract_net_protocol.py
│   ├── configuration
│   │   ├── __init__.py
│   │   └── configuration_manager.py
│   ├── data_management
│   │   ├── __init__.py
│   │   ├── backup_exceptions.py
│   │   ├── backup_purger.py
│   │   ├── backup_scheduler.py
│   │   ├── backup_storage.py
│   │   ├── data_backup_manager.py
│   │   ├── data_mapper.py
│   │   ├── data_store
│   │   │   └── data_storage.py
│   │   ├── data_transformation_manager.py
│   │   ├── data_validation_manager.py
│   │   └── repositories
│   │       ├── process_definition_repository.py
│   │       ├── process_instance_repository.py
│   │       └── repository_base.py
│   ├── error_handler.py
│   ├── event_management
│   │   └── event.py
│   ├── goal_management
│   │   ├── goal.md
│   │   └── goal.py
│   ├── knowledge_management
│   │   ├── __init__.py
│   │   ├── core
│   │   │   ├── __init__.py
│   │   │   ├── knowledge_base.py
│   │   │   └── knowledge_graph.py
│   │   ├── debugging
│   │   │   └── reasoning_debugger.py
│   │   ├── explainable_ai
│   │   │   └── reasoning_explainer.py
│   │   ├── knowledge_base
│   │   │   ├── best_practices
│   │   │   │   └── __init__.py
│   │   │   ├── industry_standards
│   │   │   │   └── __init__.py
│   │   │   └── process_templates
│   │   │       ├── __init__.py
│   │   │       └── process_template.py
│   │   ├── knowledge_extraction
│   │   │   └── __init__.py
│   │   ├── knowledge_integration
│   │   │   └── __init__.py
│   │   ├── learning
│   │   │   └── reasoning_learner.py
│   │   ├── logging
│   │   │   └── reasoning_logger.py
│   │   ├── ontology
│   │   │   ├── __init__.py
│   │   │   ├── meta_ontology.ttl
│   │   │   ├── ontology.py
│   │   │   └── ontology.ttl
│   │   ├── reasoning
│   │   │   ├── case_based_reasoner.py
│   │   │   ├── goal_plan_tree.py
│   │   │   └── htn_planner.py
│   │   ├── reasoning_engine.py
│   │   └── utils
│   │       ├── __init__.py
│   │       ├── caching.py
│   │       └── indexing.py
│   ├── localization
│   │   └── localization_manager.py
│   ├── logging
│   │   ├── __init__.py
│   │   └── logger.py
│   ├── mabos.md
│   ├── main.py
│   ├── monitoring
│   │   ├── __init__.py
│   │   ├── anomaly_detection_engine.py
│   │   ├── monitoring.py
│   │   ├── performance_metrics_collector.py
│   │   └── predictive_analytics_engine.py
│   ├── onboarding.py
│   ├── planning
│   │   ├── __init__.py
│   │   ├── plan.md
│   │   └── plan.py
│   ├── process_management
│   │   ├── __init__.py
│   │   ├── business_process_manager.py
│   │   ├── services
│   │   │   ├── __init__.py
│   │   │   └── process_optimization_engine.py
│   │   └── utils
│   │       ├── __init__.py
│   │       ├── bottleneck_identifier.py
│   │       ├── inefficiency_identifier.py
│   │       ├── optimization_suggestion_generator.py
│   │       ├── performance_metrics_calculator.py
│   │       └── suggestion_prioritizer.py
│   ├── task_management
│   │   ├── __init__.py
│   │   ├── action.py
│   │   ├── task.py
│   │   ├── task_manager.py
│   │   └── task_output.py
│   ├── user_interface.py
│   ├── user_management
│   │   ├── __init__.py
│   │   ├── authentication_manager.py
│   │   ├── authorization_manager.py
│   │   └── user.py
│   └── visualization
│       ├── __init__.py
│       └── data_visualization_manager.py
├── mabos.plantuml
├── onboarding_state_machine.plantuml
├── sdks
│   ├── README.md
│   ├── nodejs-client
│   │   ├── README.md
│   │   ├── babel.config.json
│   │   ├── index.d.ts
│   │   ├── index.js
│   │   ├── index.test.js
│   │   └── package.json
│   ├── php-client
│   │   ├── README.md
│   │   └── dify-client.php
│   └── python-client
│       ├── LICENSE
│       ├── MANIFEST.in
│       ├── README.md
│       ├── build.sh
│       ├── dify_client
│       │   ├── __init__.py
│       │   └── client.py
│       ├── setup.py
│       └── tests
│           ├── __init__.py
│           └── test_client.py
├── srd.md
└── web
    ├── Dockerfile
    ├── README.md
    ├── app
    │   ├── (commonLayout)
    │   │   ├── app
    │   │   │   └── (appDetailLayout)
    │   │   │       ├── [appId]
    │   │   │       │   ├── annotations
    │   │   │       │   │   └── page.tsx
    │   │   │       │   ├── configuration
    │   │   │       │   │   └── page.tsx
    │   │   │       │   ├── develop
    │   │   │       │   │   └── page.tsx
    │   │   │       │   ├── layout.tsx
    │   │   │       │   ├── logs
    │   │   │       │   │   └── page.tsx
    │   │   │       │   ├── overview
    │   │   │       │   │   ├── cardView.tsx
    │   │   │       │   │   ├── chartView.tsx
    │   │   │       │   │   └── page.tsx
    │   │   │       │   ├── style.module.css
    │   │   │       │   └── workflow
    │   │   │       │       └── page.tsx
    │   │   │       └── layout.tsx
    │   │   ├── apps
    │   │   │   ├── AppCard.tsx
    │   │   │   ├── Apps.tsx
    │   │   │   ├── NewAppCard.tsx
    │   │   │   ├── assets
    │   │   │   │   ├── add.svg
    │   │   │   │   ├── chat-solid.svg
    │   │   │   │   ├── chat.svg
    │   │   │   │   ├── completion-solid.svg
    │   │   │   │   ├── completion.svg
    │   │   │   │   ├── discord.svg
    │   │   │   │   ├── github.svg
    │   │   │   │   ├── link-gray.svg
    │   │   │   │   ├── link.svg
    │   │   │   │   └── right-arrow.svg
    │   │   │   ├── hooks
    │   │   │   │   └── useAppsQueryState.ts
    │   │   │   ├── page.tsx
    │   │   │   └── style.module.css
    │   │   ├── datasets
    │   │   │   ├── (datasetDetailLayout)
    │   │   │   │   ├── [datasetId]
    │   │   │   │   │   ├── api
    │   │   │   │   │   │   └── page.tsx
    │   │   │   │   │   ├── documents
    │   │   │   │   │   │   ├── [documentId]
    │   │   │   │   │   │   │   ├── page.tsx
    │   │   │   │   │   │   │   └── settings
    │   │   │   │   │   │   │       └── page.tsx
    │   │   │   │   │   │   ├── create
    │   │   │   │   │   │   │   └── page.tsx
    │   │   │   │   │   │   ├── page.tsx
    │   │   │   │   │   │   └── style.module.css
    │   │   │   │   │   ├── hitTesting
    │   │   │   │   │   │   └── page.tsx
    │   │   │   │   │   ├── layout.tsx
    │   │   │   │   │   ├── settings
    │   │   │   │   │   │   └── page.tsx
    │   │   │   │   │   └── style.module.css
    │   │   │   │   └── layout.tsx
    │   │   │   ├── ApiServer.tsx
    │   │   │   ├── Container.tsx
    │   │   │   ├── DatasetCard.tsx
    │   │   │   ├── DatasetFooter.tsx
    │   │   │   ├── Datasets.tsx
    │   │   │   ├── Doc.tsx
    │   │   │   ├── NewDatasetCard.tsx
    │   │   │   ├── create
    │   │   │   │   └── page.tsx
    │   │   │   ├── page.tsx
    │   │   │   └── template
    │   │   │       ├── template.en.mdx
    │   │   │       └── template.zh.mdx
    │   │   ├── explore
    │   │   │   ├── apps
    │   │   │   │   └── page.tsx
    │   │   │   ├── installed
    │   │   │   │   └── [appId]
    │   │   │   │       └── page.tsx
    │   │   │   └── layout.tsx
    │   │   ├── layout.tsx
    │   │   ├── list.module.css
    │   │   └── tools
    │   │       ├── custom
    │   │       │   └── page.tsx
    │   │       ├── page.tsx
    │   │       └── third-part
    │   │           └── page.tsx
    │   ├── (shareLayout)
    │   │   ├── chat
    │   │   │   └── [token]
    │   │   │       └── page.tsx
    │   │   ├── chatbot
    │   │   │   └── [token]
    │   │   │       └── page.tsx
    │   │   ├── completion
    │   │   │   └── [token]
    │   │   │       └── page.tsx
    │   │   ├── layout.tsx
    │   │   ├── webapp-signin
    │   │   │   └── page.tsx
    │   │   └── workflow
    │   │       └── [token]
    │   │           └── page.tsx
    │   ├── activate
    │   │   ├── activateForm.tsx
    │   │   ├── page.tsx
    │   │   ├── style.module.css
    │   │   └── team-28x28.png
    │   ├── components
    │   │   ├── app
    │   │   │   ├── annotation
    │   │   │   │   ├── add-annotation-modal
    │   │   │   │   │   ├── edit-item
    │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── batch-add-annotation-modal
    │   │   │   │   │   ├── csv-downloader.tsx
    │   │   │   │   │   ├── csv-uploader.tsx
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── edit-annotation-modal
    │   │   │   │   │   ├── edit-item
    │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── empty-element.tsx
    │   │   │   │   ├── filter.tsx
    │   │   │   │   ├── header-opts
    │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   └── style.module.css
    │   │   │   │   ├── index.tsx
    │   │   │   │   ├── list.tsx
    │   │   │   │   ├── remove-annotation-confirm-modal
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── style.module.css
    │   │   │   │   ├── type.ts
    │   │   │   │   └── view-annotation-modal
    │   │   │   │       ├── hit-history-no-data.tsx
    │   │   │   │       ├── index.tsx
    │   │   │   │       └── style.module.css
    │   │   │   ├── app-publisher
    │   │   │   │   ├── index.tsx
    │   │   │   │   ├── publish-with-multiple-model.tsx
    │   │   │   │   └── suggested-action.tsx
    │   │   │   ├── chat
    │   │   │   │   ├── answer
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── citation
    │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   ├── popup.tsx
    │   │   │   │   │   ├── progress-tooltip.tsx
    │   │   │   │   │   └── tooltip.tsx
    │   │   │   │   ├── copy-btn
    │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   └── style.module.css
    │   │   │   │   ├── icon-component
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── icons
    │   │   │   │   │   ├── answer.svg
    │   │   │   │   │   ├── default-avatar.jpg
    │   │   │   │   │   ├── edit.svg
    │   │   │   │   │   ├── question.svg
    │   │   │   │   │   ├── robot.svg
    │   │   │   │   │   ├── send-active.svg
    │   │   │   │   │   ├── send.svg
    │   │   │   │   │   ├── typing.svg
    │   │   │   │   │   └── user.svg
    │   │   │   │   ├── index.tsx
    │   │   │   │   ├── loading-anim
    │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   └── style.module.css
    │   │   │   │   ├── log
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── mermaid
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── more-info
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── operation
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── question
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── style.module.css
    │   │   │   │   ├── svg
    │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   └── style.module.css
    │   │   │   │   ├── thought
    │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   ├── panel.tsx
    │   │   │   │   │   ├── style.module.css
    │   │   │   │   │   └── tool.tsx
    │   │   │   │   └── type.ts
    │   │   │   ├── configuration
    │   │   │   │   ├── base
    │   │   │   │   │   ├── feature-panel
    │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   ├── group-name
    │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   ├── icons
    │   │   │   │   │   │   ├── citation.tsx
    │   │   │   │   │   │   ├── more-like-this-icon.tsx
    │   │   │   │   │   │   ├── remove-icon
    │   │   │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   │   │   └── style.module.css
    │   │   │   │   │   │   └── suggested-questions-after-answer-icon.tsx
    │   │   │   │   │   ├── operation-btn
    │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   ├── var-highlight
    │   │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   │   └── style.module.css
    │   │   │   │   │   └── warning-mask
    │   │   │   │   │       ├── cannot-query-dataset.tsx
    │   │   │   │   │       ├── formatting-changed.tsx
    │   │   │   │   │       ├── has-not-set-api.tsx
    │   │   │   │   │       ├── index.tsx
    │   │   │   │   │       └── style.module.css
    │   │   │   │   ├── config
    │   │   │   │   │   ├── agent
    │   │   │   │   │   │   ├── agent-setting
    │   │   │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   │   │   └── item-panel.tsx
    │   │   │   │   │   │   ├── agent-tools
    │   │   │   │   │   │   │   ├── choose-tool
    │   │   │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   │   │   └── setting-built-in-tool.tsx
    │   │   │   │   │   │   └── prompt-editor.tsx
    │   │   │   │   │   ├── agent-setting-button.tsx
    │   │   │   │   │   ├── assistant-type-picker
    │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   ├── automatic
    │   │   │   │   │   │   ├── automatic-btn.tsx
    │   │   │   │   │   │   └── get-automatic-res.tsx
    │   │   │   │   │   ├── feature
    │   │   │   │   │   │   ├── add-feature-btn
    │   │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   │   ├── choose-feature
    │   │   │   │   │   │   │   ├── feature-item
    │   │   │   │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   │   │   │   ├── preview-imgs
    │   │   │   │   │   │   │   │   │   ├── citation.svg
    │   │   │   │   │   │   │   │   │   ├── citations-and-attributions-preview@2x.png
    │   │   │   │   │   │   │   │   │   ├── conversation-opener-preview@2x.png
    │   │   │   │   │   │   │   │   │   ├── more-like-this-preview@2x.png
    │   │   │   │   │   │   │   │   │   ├── more-like-this.svg
    │   │   │   │   │   │   │   │   │   ├── next-question-suggestion-preview@2x.png
    │   │   │   │   │   │   │   │   │   ├── opening-statement.png
    │   │   │   │   │   │   │   │   │   ├── opening-suggestion-preview@2x.png
    │   │   │   │   │   │   │   │   │   ├── speech-to-text-preview@2x.png
    │   │   │   │   │   │   │   │   │   ├── speech-to-text.svg
    │   │   │   │   │   │   │   │   │   ├── suggested-questions-after-answer.svg
    │   │   │   │   │   │   │   │   │   ├── text-to-audio-preview-assistant@2x.png
    │   │   │   │   │   │   │   │   │   └── text-to-audio-preview-completion@2x.png
    │   │   │   │   │   │   │   │   └── style.module.css
    │   │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   │   ├── feature-group
    │   │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   │   └── use-feature.tsx
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── config-prompt
    │   │   │   │   │   ├── advanced-prompt-input.tsx
    │   │   │   │   │   ├── confirm-add-var
    │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   ├── conversation-histroy
    │   │   │   │   │   │   ├── edit-modal.tsx
    │   │   │   │   │   │   └── history-panel.tsx
    │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   ├── message-type-selector.tsx
    │   │   │   │   │   ├── prompt-editor-height-resize-wrap.tsx
    │   │   │   │   │   ├── simple-prompt-input.tsx
    │   │   │   │   │   └── style.module.css
    │   │   │   │   ├── config-var
    │   │   │   │   │   ├── config-modal
    │   │   │   │   │   │   ├── field.tsx
    │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   ├── config-select
    │   │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   │   └── style.module.css
    │   │   │   │   │   ├── config-string
    │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   ├── input-type-icon.tsx
    │   │   │   │   │   ├── modal-foot.tsx
    │   │   │   │   │   ├── select-type-item
    │   │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   │   └── style.module.css
    │   │   │   │   │   ├── select-var-type.tsx
    │   │   │   │   │   └── style.module.css
    │   │   │   │   ├── config-vision
    │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   ├── param-config-content.tsx
    │   │   │   │   │   ├── param-config.tsx
    │   │   │   │   │   └── radio-group
    │   │   │   │   │       ├── index.tsx
    │   │   │   │   │       └── style.module.css
    │   │   │   │   ├── config-voice
    │   │   │   │   │   ├── param-config-content.tsx
    │   │   │   │   │   └── param-config.tsx
    │   │   │   │   ├── ctrl-btn-group
    │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   └── style.module.css
    │   │   │   │   ├── dataset-config
    │   │   │   │   │   ├── card-item
    │   │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   │   ├── item.tsx
    │   │   │   │   │   │   └── style.module.css
    │   │   │   │   │   ├── context-var
    │   │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   │   ├── style.module.css
    │   │   │   │   │   │   └── var-picker.tsx
    │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   ├── params-config
    │   │   │   │   │   │   ├── config-content.tsx
    │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   ├── select-dataset
    │   │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   │   └── style.module.css
    │   │   │   │   │   ├── settings-modal
    │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   └── type-icon
    │   │   │   │   │       └── index.tsx
    │   │   │   │   ├── debug
    │   │   │   │   │   ├── debug-with-multiple-model
    │   │   │   │   │   │   ├── chat-item.tsx
    │   │   │   │   │   │   ├── context.tsx
    │   │   │   │   │   │   ├── debug-item.tsx
    │   │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   │   ├── model-parameter-trigger.tsx
    │   │   │   │   │   │   └── text-generation-item.tsx
    │   │   │   │   │   ├── debug-with-single-model
    │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   ├── hooks.tsx
    │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   └── types.ts
    │   │   │   │   ├── features
    │   │   │   │   │   ├── chat-group
    │   │   │   │   │   │   ├── citation
    │   │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   │   ├── opening-statement
    │   │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   │   ├── speech-to-text
    │   │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   │   ├── suggested-questions-after-answer
    │   │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   │   └── text-to-speech
    │   │   │   │   │   │       └── index.tsx
    │   │   │   │   │   └── experience-enchance-group
    │   │   │   │   │       ├── index.tsx
    │   │   │   │   │       └── more-like-this
    │   │   │   │   │           └── index.tsx
    │   │   │   │   ├── hooks
    │   │   │   │   │   └── use-advanced-prompt-config.ts
    │   │   │   │   ├── images
    │   │   │   │   │   └── prompt.svg
    │   │   │   │   ├── index.tsx
    │   │   │   │   ├── prompt-mode
    │   │   │   │   │   └── advanced-mode-waring.tsx
    │   │   │   │   ├── prompt-value-panel
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── style.module.css
    │   │   │   │   ├── toolbox
    │   │   │   │   │   ├── annotation
    │   │   │   │   │   │   ├── annotation-ctrl-btn
    │   │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   │   ├── config-param-modal.tsx
    │   │   │   │   │   │   ├── config-param.tsx
    │   │   │   │   │   │   ├── type.ts
    │   │   │   │   │   │   └── use-annotation-config.ts
    │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   ├── moderation
    │   │   │   │   │   │   ├── form-generation.tsx
    │   │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   │   ├── moderation-content.tsx
    │   │   │   │   │   │   └── moderation-setting-modal.tsx
    │   │   │   │   │   └── score-slider
    │   │   │   │   │       ├── base-slider
    │   │   │   │   │       │   ├── index.tsx
    │   │   │   │   │       │   └── style.module.css
    │   │   │   │   │       └── index.tsx
    │   │   │   │   └── tools
    │   │   │   │       ├── external-data-tool-modal.tsx
    │   │   │   │       └── index.tsx
    │   │   │   ├── create-app-dialog
    │   │   │   │   ├── index.tsx
    │   │   │   │   └── newAppDialog.tsx
    │   │   │   ├── create-app-modal
    │   │   │   │   ├── advanced.png
    │   │   │   │   ├── basic.png
    │   │   │   │   ├── grid-bg-agent-chat.svg
    │   │   │   │   ├── grid-bg-chat.svg
    │   │   │   │   ├── grid-bg-completion.svg
    │   │   │   │   ├── grid-bg-workflow.svg
    │   │   │   │   ├── index.tsx
    │   │   │   │   └── style.module.css
    │   │   │   ├── create-from-dsl-modal
    │   │   │   │   ├── index.tsx
    │   │   │   │   └── uploader.tsx
    │   │   │   ├── duplicate-modal
    │   │   │   │   ├── index.tsx
    │   │   │   │   └── style.module.css
    │   │   │   ├── log
    │   │   │   │   ├── filter.tsx
    │   │   │   │   ├── index.tsx
    │   │   │   │   ├── list.tsx
    │   │   │   │   ├── style.module.css
    │   │   │   │   └── var-panel.tsx
    │   │   │   ├── log-annotation
    │   │   │   │   └── index.tsx
    │   │   │   ├── overview
    │   │   │   │   ├── apikey-info-panel
    │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   └── progress
    │   │   │   │   │       ├── index.tsx
    │   │   │   │   │       └── style.module.css
    │   │   │   │   ├── appCard.tsx
    │   │   │   │   ├── appChart.tsx
    │   │   │   │   ├── assets
    │   │   │   │   │   ├── chromeplugin-install.svg
    │   │   │   │   │   ├── chromeplugin-option.svg
    │   │   │   │   │   ├── code-browser.svg
    │   │   │   │   │   ├── iframe-option.svg
    │   │   │   │   │   ├── refresh-hover.svg
    │   │   │   │   │   ├── refresh.svg
    │   │   │   │   │   └── scripts-option.svg
    │   │   │   │   ├── customize
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── embedded
    │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   └── style.module.css
    │   │   │   │   ├── settings
    │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   └── style.module.css
    │   │   │   │   └── style.module.css
    │   │   │   ├── store.ts
    │   │   │   ├── switch-app-modal
    │   │   │   │   ├── index.tsx
    │   │   │   │   └── style.module.css
    │   │   │   ├── text-generate
    │   │   │   │   ├── index.tsx
    │   │   │   │   ├── item
    │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   └── result-tab.tsx
    │   │   │   │   └── saved-items
    │   │   │   │       ├── index.tsx
    │   │   │   │       └── no-data
    │   │   │   │           └── index.tsx
    │   │   │   ├── type-selector
    │   │   │   │   └── index.tsx
    │   │   │   └── workflow-log
    │   │   │       ├── detail.tsx
    │   │   │       ├── filter.tsx
    │   │   │       ├── index.tsx
    │   │   │       ├── list.tsx
    │   │   │       └── style.module.css
    │   │   ├── app-sidebar
    │   │   │   ├── app-info.tsx
    │   │   │   ├── basic.tsx
    │   │   │   ├── completion.png
    │   │   │   ├── expert.png
    │   │   │   ├── index.tsx
    │   │   │   ├── navLink.tsx
    │   │   │   └── style.module.css
    │   │   ├── base
    │   │   │   ├── agent-log-modal
    │   │   │   │   ├── detail.tsx
    │   │   │   │   ├── index.tsx
    │   │   │   │   ├── iteration.tsx
    │   │   │   │   ├── result.tsx
    │   │   │   │   ├── tool-call.tsx
    │   │   │   │   └── tracing.tsx
    │   │   │   ├── app-icon
    │   │   │   │   ├── index.tsx
    │   │   │   │   └── style.module.css
    │   │   │   ├── app-unavailable.tsx
    │   │   │   ├── audio-btn
    │   │   │   │   ├── index.tsx
    │   │   │   │   └── style.module.css
    │   │   │   ├── auto-height-textarea
    │   │   │   │   ├── common.tsx
    │   │   │   │   ├── index.tsx
    │   │   │   │   └── style.module.scss
    │   │   │   ├── avatar
    │   │   │   │   └── index.tsx
    │   │   │   ├── block-input
    │   │   │   │   └── index.tsx
    │   │   │   ├── button
    │   │   │   │   ├── add-button.tsx
    │   │   │   │   ├── index.css
    │   │   │   │   └── index.tsx
    │   │   │   ├── chat
    │   │   │   │   ├── chat
    │   │   │   │   │   ├── answer
    │   │   │   │   │   │   ├── agent-content.tsx
    │   │   │   │   │   │   ├── basic-content.tsx
    │   │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   │   ├── more.tsx
    │   │   │   │   │   │   ├── operation.tsx
    │   │   │   │   │   │   ├── suggested-questions.tsx
    │   │   │   │   │   │   └── workflow-process.tsx
    │   │   │   │   │   ├── chat-input.tsx
    │   │   │   │   │   ├── context.tsx
    │   │   │   │   │   ├── hooks.ts
    │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   ├── question.tsx
    │   │   │   │   │   └── try-to-ask.tsx
    │   │   │   │   ├── chat-with-history
    │   │   │   │   │   ├── chat-wrapper.tsx
    │   │   │   │   │   ├── config-panel
    │   │   │   │   │   │   ├── form-input.tsx
    │   │   │   │   │   │   ├── form.tsx
    │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   ├── context.tsx
    │   │   │   │   │   ├── header-in-mobile.tsx
    │   │   │   │   │   ├── header.tsx
    │   │   │   │   │   ├── hooks.tsx
    │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   └── sidebar
    │   │   │   │   │       ├── index.tsx
    │   │   │   │   │       ├── item.tsx
    │   │   │   │   │       └── list.tsx
    │   │   │   │   ├── constants.ts
    │   │   │   │   └── types.ts
    │   │   │   ├── checkbox
    │   │   │   │   ├── assets
    │   │   │   │   │   └── check.svg
    │   │   │   │   ├── index.module.css
    │   │   │   │   └── index.tsx
    │   │   │   ├── confirm
    │   │   │   │   ├── common.module.css
    │   │   │   │   ├── common.tsx
    │   │   │   │   └── index.tsx
    │   │   │   ├── confirm-ui
    │   │   │   │   └── index.tsx
    │   │   │   ├── copy-feedback
    │   │   │   │   ├── index.tsx
    │   │   │   │   └── style.module.css
    │   │   │   ├── custom-icon
    │   │   │   │   └── index.tsx
    │   │   │   ├── dialog
    │   │   │   │   └── index.tsx
    │   │   │   ├── divider
    │   │   │   │   ├── index.tsx
    │   │   │   │   └── style.module.css
    │   │   │   ├── drawer
    │   │   │   │   └── index.tsx
    │   │   │   ├── drawer-plus
    │   │   │   │   └── index.tsx
    │   │   │   ├── dropdown
    │   │   │   │   └── index.tsx
    │   │   │   ├── emoji-picker
    │   │   │   │   ├── index.tsx
    │   │   │   │   └── style.module.css
    │   │   │   ├── features
    │   │   │   │   ├── context.tsx
    │   │   │   │   ├── feature-choose
    │   │   │   │   │   ├── feature-group
    │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   ├── feature-item
    │   │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   │   ├── preview-imgs
    │   │   │   │   │   │   │   ├── citation.svg
    │   │   │   │   │   │   │   ├── citations-and-attributions-preview@2x.png
    │   │   │   │   │   │   │   ├── conversation-opener-preview@2x.png
    │   │   │   │   │   │   │   ├── more-like-this-preview@2x.png
    │   │   │   │   │   │   │   ├── more-like-this.svg
    │   │   │   │   │   │   │   ├── next-question-suggestion-preview@2x.png
    │   │   │   │   │   │   │   ├── opening-statement.png
    │   │   │   │   │   │   │   ├── opening-suggestion-preview@2x.png
    │   │   │   │   │   │   │   ├── speech-to-text-preview@2x.png
    │   │   │   │   │   │   │   ├── speech-to-text.svg
    │   │   │   │   │   │   │   ├── suggested-questions-after-answer.svg
    │   │   │   │   │   │   │   ├── text-to-audio-preview-assistant@2x.png
    │   │   │   │   │   │   │   └── text-to-audio-preview-completion@2x.png
    │   │   │   │   │   │   └── style.module.css
    │   │   │   │   │   ├── feature-modal.tsx
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── feature-panel
    │   │   │   │   │   ├── citation
    │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   ├── file-upload
    │   │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   │   ├── param-config-content.tsx
    │   │   │   │   │   │   ├── param-config.tsx
    │   │   │   │   │   │   └── radio-group
    │   │   │   │   │   │       ├── index.tsx
    │   │   │   │   │   │       └── style.module.css
    │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   ├── moderation
    │   │   │   │   │   │   ├── form-generation.tsx
    │   │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   │   ├── moderation-content.tsx
    │   │   │   │   │   │   └── moderation-setting-modal.tsx
    │   │   │   │   │   ├── opening-statement
    │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   ├── score-slider
    │   │   │   │   │   │   ├── base-slider
    │   │   │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   │   │   └── style.module.css
    │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   ├── speech-to-text
    │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   ├── suggested-questions-after-answer
    │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   └── text-to-speech
    │   │   │   │   │       ├── index.tsx
    │   │   │   │   │       ├── param-config-content.tsx
    │   │   │   │   │       └── params-config.tsx
    │   │   │   │   ├── hooks.ts
    │   │   │   │   ├── index.tsx
    │   │   │   │   ├── store.ts
    │   │   │   │   └── types.ts
    │   │   │   ├── file-icon
    │   │   │   │   └── index.tsx
    │   │   │   ├── float-popover-container
    │   │   │   │   └── index.tsx
    │   │   │   ├── float-right-container
    │   │   │   │   └── index.tsx
    │   │   │   ├── ga
    │   │   │   │   └── index.tsx
    │   │   │   ├── grid-mask
    │   │   │   │   └── index.tsx
    │   │   │   ├── icons
    │   │   │   │   ├── IconBase.tsx
    │   │   │   │   ├── assets
    │   │   │   │   │   ├── image
    │   │   │   │   │   │   └── llm
    │   │   │   │   │   │       ├── baichuan-text-cn.png
    │   │   │   │   │   │       ├── minimax-text.png
    │   │   │   │   │   │       ├── minimax.png
    │   │   │   │   │   │       ├── tongyi-text-cn.png
    │   │   │   │   │   │       ├── tongyi-text.png
    │   │   │   │   │   │       ├── tongyi.png
    │   │   │   │   │   │       ├── wxyy-text-cn.png
    │   │   │   │   │   │       ├── wxyy-text.png
    │   │   │   │   │   │       └── wxyy.png
    │   │   │   │   │   ├── public
    │   │   │   │   │   │   ├── avatar
    │   │   │   │   │   │   │   ├── robot.svg
    │   │   │   │   │   │   │   └── user.svg
    │   │   │   │   │   │   ├── billing
    │   │   │   │   │   │   │   └── sparkles.svg
    │   │   │   │   │   │   ├── common
    │   │   │   │   │   │   │   ├── diagonal-dividing-line.svg
    │   │   │   │   │   │   │   ├── dify.svg
    │   │   │   │   │   │   │   ├── github.svg
    │   │   │   │   │   │   │   ├── line-3.svg
    │   │   │   │   │   │   │   ├── message-chat-square.svg
    │   │   │   │   │   │   │   ├── multi-path-retrieval.svg
    │   │   │   │   │   │   │   ├── n-to-1-retrieval.svg
    │   │   │   │   │   │   │   └── notion.svg
    │   │   │   │   │   │   ├── files
    │   │   │   │   │   │   │   ├── csv.svg
    │   │   │   │   │   │   │   ├── doc.svg
    │   │   │   │   │   │   │   ├── docx.svg
    │   │   │   │   │   │   │   ├── html.svg
    │   │   │   │   │   │   │   ├── json.svg
    │   │   │   │   │   │   │   ├── md.svg
    │   │   │   │   │   │   │   ├── pdf.svg
    │   │   │   │   │   │   │   ├── txt.svg
    │   │   │   │   │   │   │   ├── unknow.svg
    │   │   │   │   │   │   │   ├── xlsx.svg
    │   │   │   │   │   │   │   └── yaml.svg
    │   │   │   │   │   │   ├── header-nav
    │   │   │   │   │   │   │   ├── explore
    │   │   │   │   │   │   │   │   ├── explore-active.svg
    │   │   │   │   │   │   │   │   └── explore.svg
    │   │   │   │   │   │   │   ├── knowledge
    │   │   │   │   │   │   │   │   ├── knowledge-active.svg
    │   │   │   │   │   │   │   │   └── knowledge.svg
    │   │   │   │   │   │   │   ├── studio
    │   │   │   │   │   │   │   │   ├── Robot-Active.svg
    │   │   │   │   │   │   │   │   └── Robot.svg
    │   │   │   │   │   │   │   └── tools
    │   │   │   │   │   │   │       ├── tools-active.svg
    │   │   │   │   │   │   │       └── tools.svg
    │   │   │   │   │   │   ├── llm
    │   │   │   │   │   │   │   ├── anthropic-text.svg
    │   │   │   │   │   │   │   ├── anthropic.svg
    │   │   │   │   │   │   │   ├── azure-openai-service-text.svg
    │   │   │   │   │   │   │   ├── azure-openai-service.svg
    │   │   │   │   │   │   │   ├── azureai-text.svg
    │   │   │   │   │   │   │   ├── azureai.svg
    │   │   │   │   │   │   │   ├── baichuan-text.svg
    │   │   │   │   │   │   │   ├── baichuan.svg
    │   │   │   │   │   │   │   ├── chatglm-text.svg
    │   │   │   │   │   │   │   ├── chatglm.svg
    │   │   │   │   │   │   │   ├── cohere-text.svg
    │   │   │   │   │   │   │   ├── cohere.svg
    │   │   │   │   │   │   │   ├── gpt-3.svg
    │   │   │   │   │   │   │   ├── gpt-4.svg
    │   │   │   │   │   │   │   ├── huggingface-text-hub.svg
    │   │   │   │   │   │   │   ├── huggingface-text.svg
    │   │   │   │   │   │   │   ├── huggingface.svg
    │   │   │   │   │   │   │   ├── iflytek-spark-text-cn.svg
    │   │   │   │   │   │   │   ├── iflytek-spark-text.svg
    │   │   │   │   │   │   │   ├── iflytek-spark.svg
    │   │   │   │   │   │   │   ├── jina-text.svg
    │   │   │   │   │   │   │   ├── jina.svg
    │   │   │   │   │   │   │   ├── localai-text.svg
    │   │   │   │   │   │   │   ├── localai.svg
    │   │   │   │   │   │   │   ├── microsoft.svg
    │   │   │   │   │   │   │   ├── openai-black.svg
    │   │   │   │   │   │   │   ├── openai-blue.svg
    │   │   │   │   │   │   │   ├── openai-green.svg
    │   │   │   │   │   │   │   ├── openai-text.svg
    │   │   │   │   │   │   │   ├── openai-transparent.svg
    │   │   │   │   │   │   │   ├── openai-violet.svg
    │   │   │   │   │   │   │   ├── openllm-text.svg
    │   │   │   │   │   │   │   ├── openllm.svg
    │   │   │   │   │   │   │   ├── replicate-text.svg
    │   │   │   │   │   │   │   ├── replicate.svg
    │   │   │   │   │   │   │   ├── xorbits-inference-text.svg
    │   │   │   │   │   │   │   ├── xorbits-inference.svg
    │   │   │   │   │   │   │   ├── zhipuai-text-cn.svg
    │   │   │   │   │   │   │   ├── zhipuai-text.svg
    │   │   │   │   │   │   │   └── zhipuai.svg
    │   │   │   │   │   │   ├── model
    │   │   │   │   │   │   │   └── checked.svg
    │   │   │   │   │   │   ├── other
    │   │   │   │   │   │   │   ├── Icon-3-dots.svg
    │   │   │   │   │   │   │   └── default-tool-icon.svg
    │   │   │   │   │   │   ├── plugins
    │   │   │   │   │   │   │   ├── google.svg
    │   │   │   │   │   │   │   ├── web-reader.svg
    │   │   │   │   │   │   │   └── wikipedia.svg
    │   │   │   │   │   │   └── thought
    │   │   │   │   │   │       ├── data-set.svg
    │   │   │   │   │   │       ├── loading.svg
    │   │   │   │   │   │       ├── search.svg
    │   │   │   │   │   │       ├── thought-list.svg
    │   │   │   │   │   │       └── web-reader.svg
    │   │   │   │   │   └── vender
    │   │   │   │   │       ├── line
    │   │   │   │   │       │   ├── alertsAndFeedback
    │   │   │   │   │       │   │   ├── alert-circle.svg
    │   │   │   │   │       │   │   ├── alert-triangle.svg
    │   │   │   │   │       │   │   ├── thumbs-down.svg
    │   │   │   │   │       │   │   └── thumbs-up.svg
    │   │   │   │   │       │   ├── arrows
    │   │   │   │   │       │   │   ├── arrow-narrow-left.svg
    │   │   │   │   │       │   │   ├── arrow-narrow-right.svg
    │   │   │   │   │       │   │   ├── arrow-up-right.svg
    │   │   │   │   │       │   │   ├── chevron-down-double.svg
    │   │   │   │   │       │   │   ├── chevron-down.svg
    │   │   │   │   │       │   │   ├── chevron-right.svg
    │   │   │   │   │       │   │   ├── chevron-selector-vertical.svg
    │   │   │   │   │       │   │   ├── collapse-04.svg
    │   │   │   │   │       │   │   ├── flip-backward.svg
    │   │   │   │   │       │   │   ├── flip-forward.svg
    │   │   │   │   │       │   │   ├── refresh-ccw-01.svg
    │   │   │   │   │       │   │   ├── refresh-cw-05.svg
    │   │   │   │   │       │   │   └── reverse-left.svg
    │   │   │   │   │       │   ├── communication
    │   │   │   │   │       │   │   ├── ai-text.svg
    │   │   │   │   │       │   │   ├── chat-bot-slim.svg
    │   │   │   │   │       │   │   ├── chat-bot.svg
    │   │   │   │   │       │   │   ├── cute-robot.svg
    │   │   │   │   │       │   │   ├── message-check-remove.svg
    │   │   │   │   │       │   │   ├── message-fast-plus.svg
    │   │   │   │   │       │   │   └── message-play.svg
    │   │   │   │   │       │   ├── development
    │   │   │   │   │       │   │   ├── artificial-brain.svg
    │   │   │   │   │       │   │   ├── bar-chart-square-02.svg
    │   │   │   │   │       │   │   ├── brackets-x.svg
    │   │   │   │   │       │   │   ├── code-browser.svg
    │   │   │   │   │       │   │   ├── container.svg
    │   │   │   │   │       │   │   ├── database-01.svg
    │   │   │   │   │       │   │   ├── database-03.svg
    │   │   │   │   │       │   │   ├── file-heart-02.svg
    │   │   │   │   │       │   │   ├── git-branch-01.svg
    │   │   │   │   │       │   │   ├── prompt-engineering.svg
    │   │   │   │   │       │   │   ├── puzzle-piece-01.svg
    │   │   │   │   │       │   │   ├── terminal-square.svg
    │   │   │   │   │       │   │   ├── variable.svg
    │   │   │   │   │       │   │   └── webhooks.svg
    │   │   │   │   │       │   ├── editor
    │   │   │   │   │       │   │   ├── align-left.svg
    │   │   │   │   │       │   │   ├── bezier-curve-03.svg
    │   │   │   │   │       │   │   ├── colors.svg
    │   │   │   │   │       │   │   ├── cursor-02c.svg
    │   │   │   │   │       │   │   ├── hand-02.svg
    │   │   │   │   │       │   │   ├── image-indent-left.svg
    │   │   │   │   │       │   │   ├── left-indent-02.svg
    │   │   │   │   │       │   │   ├── letter-spacing-01.svg
    │   │   │   │   │       │   │   ├── type-square.svg
    │   │   │   │   │       │   │   ├── zoom-in.svg
    │   │   │   │   │       │   │   └── zoom-out.svg
    │   │   │   │   │       │   ├── education
    │   │   │   │   │       │   │   └── book-open-01.svg
    │   │   │   │   │       │   ├── files
    │   │   │   │   │       │   │   ├── clipboard-check.svg
    │   │   │   │   │       │   │   ├── clipboard.svg
    │   │   │   │   │       │   │   ├── file-02.svg
    │   │   │   │   │       │   │   ├── file-arrow-01.svg
    │   │   │   │   │       │   │   ├── file-check-02.svg
    │   │   │   │   │       │   │   ├── file-download-02.svg
    │   │   │   │   │       │   │   ├── file-plus-01.svg
    │   │   │   │   │       │   │   ├── file-plus-02.svg
    │   │   │   │   │       │   │   └── file-text.svg
    │   │   │   │   │       │   ├── financeAndECommerce
    │   │   │   │   │       │   │   ├── coins-stacked-01.svg
    │   │   │   │   │       │   │   ├── gold-coin.svg
    │   │   │   │   │       │   │   ├── receipt-list.svg
    │   │   │   │   │       │   │   ├── tag-01.svg
    │   │   │   │   │       │   │   └── tag-03.svg
    │   │   │   │   │       │   ├── general
    │   │   │   │   │       │   │   ├── Workflow.zip
    │   │   │   │   │       │   │   ├── at-sign.svg
    │   │   │   │   │       │   │   ├── bookmark.svg
    │   │   │   │   │       │   │   ├── check-circle.svg
    │   │   │   │   │       │   │   ├── check-done-01.svg
    │   │   │   │   │       │   │   ├── check.svg
    │   │   │   │   │       │   │   ├── checklist-square.svg
    │   │   │   │   │       │   │   ├── checklist.svg
    │   │   │   │   │       │   │   ├── dots-grid.svg
    │   │   │   │   │       │   │   ├── dots-horizontal.svg
    │   │   │   │   │       │   │   ├── edit-02.svg
    │   │   │   │   │       │   │   ├── edit-03.svg
    │   │   │   │   │       │   │   ├── edit-04.svg
    │   │   │   │   │       │   │   ├── edit-05.svg
    │   │   │   │   │       │   │   ├── hash-02.svg
    │   │   │   │   │       │   │   ├── help-circle.svg
    │   │   │   │   │       │   │   ├── info-circle.svg
    │   │   │   │   │       │   │   ├── link-03.svg
    │   │   │   │   │       │   │   ├── link-external-01.svg
    │   │   │   │   │       │   │   ├── link-external-02.svg
    │   │   │   │   │       │   │   ├── loading-02.svg
    │   │   │   │   │       │   │   ├── log-in-04.svg
    │   │   │   │   │       │   │   ├── log-out-01.svg
    │   │   │   │   │       │   │   ├── log-out-04.svg
    │   │   │   │   │       │   │   ├── menu-01.svg
    │   │   │   │   │       │   │   ├── pin-01.svg
    │   │   │   │   │       │   │   ├── pin-02.svg
    │   │   │   │   │       │   │   ├── plus-02.svg
    │   │   │   │   │       │   │   ├── plus.svg
    │   │   │   │   │       │   │   ├── search-lg.svg
    │   │   │   │   │       │   │   ├── settings-01.svg
    │   │   │   │   │       │   │   ├── settings-04.svg
    │   │   │   │   │       │   │   ├── target-04.svg
    │   │   │   │   │       │   │   ├── trash-03.svg
    │   │   │   │   │       │   │   ├── upload-03.svg
    │   │   │   │   │       │   │   ├── upload-cloud-01.svg
    │   │   │   │   │       │   │   ├── x-close.svg
    │   │   │   │   │       │   │   └── x.svg
    │   │   │   │   │       │   ├── images
    │   │   │   │   │       │   │   └── image-plus.svg
    │   │   │   │   │       │   ├── layout
    │   │   │   │   │       │   │   ├── align-left-01.svg
    │   │   │   │   │       │   │   ├── align-right-01.svg
    │   │   │   │   │       │   │   ├── grid-01.svg
    │   │   │   │   │       │   │   ├── layout-grid-02.svg
    │   │   │   │   │       │   │   └── organize-grid.svg
    │   │   │   │   │       │   ├── mapsAndTravel
    │   │   │   │   │       │   │   ├── globe-01.svg
    │   │   │   │   │       │   │   └── route.svg
    │   │   │   │   │       │   ├── mediaAndDevices
    │   │   │   │   │       │   │   ├── microphone-01.svg
    │   │   │   │   │       │   │   ├── play-circle.svg
    │   │   │   │   │       │   │   ├── play.svg
    │   │   │   │   │       │   │   ├── sliders-h.svg
    │   │   │   │   │       │   │   ├── speaker.svg
    │   │   │   │   │       │   │   ├── stop-circle.svg
    │   │   │   │   │       │   │   └── stop.svg
    │   │   │   │   │       │   ├── others
    │   │   │   │   │       │   │   └── drag-handle.svg
    │   │   │   │   │       │   ├── shapes
    │   │   │   │   │       │   │   └── cube-outline.svg
    │   │   │   │   │       │   ├── time
    │   │   │   │   │       │   │   ├── clock-fast-forward.svg
    │   │   │   │   │       │   │   ├── clock-play-slim.svg
    │   │   │   │   │       │   │   ├── clock-play.svg
    │   │   │   │   │       │   │   └── clock-refresh.svg
    │   │   │   │   │       │   ├── users
    │   │   │   │   │       │   │   ├── user-01.svg
    │   │   │   │   │       │   │   └── users-01.svg
    │   │   │   │   │       │   └── weather
    │   │   │   │   │       │       └── stars-02.svg
    │   │   │   │   │       ├── solid
    │   │   │   │   │       │   ├── FinanceAndECommerce
    │   │   │   │   │       │   │   ├── gold-coin.svg
    │   │   │   │   │       │   │   └── scales-02.svg
    │   │   │   │   │       │   ├── alertsAndFeedback
    │   │   │   │   │       │   │   ├── alert-circle.svg
    │   │   │   │   │       │   │   └── alert-triangle.svg
    │   │   │   │   │       │   ├── arrows
    │   │   │   │   │       │   │   ├── chevron-down.svg
    │   │   │   │   │       │   │   ├── expand-04.svg
    │   │   │   │   │       │   │   └── high-priority.svg
    │   │   │   │   │       │   ├── communication
    │   │   │   │   │       │   │   ├── ai-text.svg
    │   │   │   │   │       │   │   ├── chat-bot.svg
    │   │   │   │   │       │   │   ├── cute-robote.svg
    │   │   │   │   │       │   │   ├── edit-list.svg
    │   │   │   │   │       │   │   ├── message-dots-circle.svg
    │   │   │   │   │       │   │   ├── message-fast.svg
    │   │   │   │   │       │   │   ├── message-heart-circle.svg
    │   │   │   │   │       │   │   ├── message-smile-square.svg
    │   │   │   │   │       │   │   └── send-03.svg
    │   │   │   │   │       │   ├── development
    │   │   │   │   │       │   │   ├── api-connection.svg
    │   │   │   │   │       │   │   ├── bar-chart-square-02.svg
    │   │   │   │   │       │   │   ├── container.svg
    │   │   │   │   │       │   │   ├── database-02.svg
    │   │   │   │   │       │   │   ├── database-03.svg
    │   │   │   │   │       │   │   ├── file-heart-02.svg
    │   │   │   │   │       │   │   ├── pattern-recognition.svg
    │   │   │   │   │       │   │   ├── prompt-engineering.svg
    │   │   │   │   │       │   │   ├── puzzle-piece-01.svg
    │   │   │   │   │       │   │   ├── semantic.svg
    │   │   │   │   │       │   │   ├── terminal-square.svg
    │   │   │   │   │       │   │   └── variable-02.svg
    │   │   │   │   │       │   ├── editor
    │   │   │   │   │       │   │   ├── brush-01.svg
    │   │   │   │   │       │   │   ├── citations.svg
    │   │   │   │   │       │   │   ├── colors.svg
    │   │   │   │   │       │   │   ├── cursor-02c.svg
    │   │   │   │   │       │   │   ├── hand-02.svg
    │   │   │   │   │       │   │   ├── paragraph.svg
    │   │   │   │   │       │   │   └── type-square.svg
    │   │   │   │   │       │   ├── education
    │   │   │   │   │       │   │   ├── beaker-02.svg
    │   │   │   │   │       │   │   ├── bubble-text.svg
    │   │   │   │   │       │   │   ├── heart-02.svg
    │   │   │   │   │       │   │   └── unblur.svg
    │   │   │   │   │       │   ├── files
    │   │   │   │   │       │   │   ├── file-05.svg
    │   │   │   │   │       │   │   ├── file-search-02.svg
    │   │   │   │   │       │   │   └── folder.svg
    │   │   │   │   │       │   ├── general
    │   │   │   │   │       │   │   ├── answer-triangle.svg
    │   │   │   │   │       │   │   ├── check-circle.svg
    │   │   │   │   │       │   │   ├── check-done-01.svg
    │   │   │   │   │       │   │   ├── download-02.svg
    │   │   │   │   │       │   │   ├── edit-03.svg
    │   │   │   │   │       │   │   ├── edit-04.svg
    │   │   │   │   │       │   │   ├── eye.svg
    │   │   │   │   │       │   │   ├── message-clock-circle.svg
    │   │   │   │   │       │   │   ├── plus-circle.svg
    │   │   │   │   │       │   │   ├── question-triangle.svg
    │   │   │   │   │       │   │   ├── search-md.svg
    │   │   │   │   │       │   │   ├── target-04.svg
    │   │   │   │   │       │   │   ├── tool-03.svg
    │   │   │   │   │       │   │   ├── x-circle.svg
    │   │   │   │   │       │   │   ├── zap-fast.svg
    │   │   │   │   │       │   │   └── zap-narrow.svg
    │   │   │   │   │       │   ├── layout
    │   │   │   │   │       │   │   └── grid-01.svg
    │   │   │   │   │       │   ├── mapsAndTravel
    │   │   │   │   │       │   │   └── route.svg
    │   │   │   │   │       │   ├── mediaAndDevices
    │   │   │   │   │       │   │   ├── magic-box.svg
    │   │   │   │   │       │   │   ├── magic-eyes.svg
    │   │   │   │   │       │   │   ├── magic-wand.svg
    │   │   │   │   │       │   │   ├── microphone-01.svg
    │   │   │   │   │       │   │   ├── play.svg
    │   │   │   │   │       │   │   ├── robot.svg
    │   │   │   │   │       │   │   ├── sliders-02.svg
    │   │   │   │   │       │   │   ├── speaker.svg
    │   │   │   │   │       │   │   └── stop-circle.svg
    │   │   │   │   │       │   ├── security
    │   │   │   │   │       │   │   └── lock-01.svg
    │   │   │   │   │       │   ├── shapes
    │   │   │   │   │       │   │   ├── star-04.svg
    │   │   │   │   │       │   │   └── star-06.svg
    │   │   │   │   │       │   └── users
    │   │   │   │   │       │       ├── user-01.svg
    │   │   │   │   │       │       ├── user-edit-02.svg
    │   │   │   │   │       │       └── users-01.svg
    │   │   │   │   │       └── workflow
    │   │   │   │   │           ├── answer.svg
    │   │   │   │   │           ├── code.svg
    │   │   │   │   │           ├── end.svg
    │   │   │   │   │           ├── home.svg
    │   │   │   │   │           ├── http.svg
    │   │   │   │   │           ├── if-else.svg
    │   │   │   │   │           ├── jinja.svg
    │   │   │   │   │           ├── knowledge-retrieval.svg
    │   │   │   │   │           ├── llm.svg
    │   │   │   │   │           ├── question-classifier.svg
    │   │   │   │   │           ├── templating-transform.svg
    │   │   │   │   │           └── variable-x.svg
    │   │   │   │   ├── script.js
    │   │   │   │   ├── src
    │   │   │   │   │   ├── image
    │   │   │   │   │   │   └── llm
    │   │   │   │   │   │       ├── BaichuanTextCn.module.css
    │   │   │   │   │   │       ├── BaichuanTextCn.tsx
    │   │   │   │   │   │       ├── Minimax.module.css
    │   │   │   │   │   │       ├── Minimax.tsx
    │   │   │   │   │   │       ├── MinimaxText.module.css
    │   │   │   │   │   │       ├── MinimaxText.tsx
    │   │   │   │   │   │       ├── Tongyi.module.css
    │   │   │   │   │   │       ├── Tongyi.tsx
    │   │   │   │   │   │       ├── TongyiText.module.css
    │   │   │   │   │   │       ├── TongyiText.tsx
    │   │   │   │   │   │       ├── TongyiTextCn.module.css
    │   │   │   │   │   │       ├── TongyiTextCn.tsx
    │   │   │   │   │   │       ├── Wxyy.module.css
    │   │   │   │   │   │       ├── Wxyy.tsx
    │   │   │   │   │   │       ├── WxyyText.module.css
    │   │   │   │   │   │       ├── WxyyText.tsx
    │   │   │   │   │   │       ├── WxyyTextCn.module.css
    │   │   │   │   │   │       ├── WxyyTextCn.tsx
    │   │   │   │   │   │       └── index.ts
    │   │   │   │   │   ├── public
    │   │   │   │   │   │   ├── avatar
    │   │   │   │   │   │   │   ├── Robot.json
    │   │   │   │   │   │   │   ├── Robot.tsx
    │   │   │   │   │   │   │   ├── User.json
    │   │   │   │   │   │   │   ├── User.tsx
    │   │   │   │   │   │   │   └── index.ts
    │   │   │   │   │   │   ├── billing
    │   │   │   │   │   │   │   ├── Sparkles.json
    │   │   │   │   │   │   │   ├── Sparkles.tsx
    │   │   │   │   │   │   │   └── index.ts
    │   │   │   │   │   │   ├── common
    │   │   │   │   │   │   │   ├── DiagonalDividingLine.json
    │   │   │   │   │   │   │   ├── DiagonalDividingLine.tsx
    │   │   │   │   │   │   │   ├── Dify.json
    │   │   │   │   │   │   │   ├── Dify.tsx
    │   │   │   │   │   │   │   ├── Github.json
    │   │   │   │   │   │   │   ├── Github.tsx
    │   │   │   │   │   │   │   ├── Line3.json
    │   │   │   │   │   │   │   ├── Line3.tsx
    │   │   │   │   │   │   │   ├── MessageChatSquare.json
    │   │   │   │   │   │   │   ├── MessageChatSquare.tsx
    │   │   │   │   │   │   │   ├── MultiPathRetrieval.json
    │   │   │   │   │   │   │   ├── MultiPathRetrieval.tsx
    │   │   │   │   │   │   │   ├── NTo1Retrieval.json
    │   │   │   │   │   │   │   ├── NTo1Retrieval.tsx
    │   │   │   │   │   │   │   ├── Notion.json
    │   │   │   │   │   │   │   ├── Notion.tsx
    │   │   │   │   │   │   │   └── index.ts
    │   │   │   │   │   │   ├── files
    │   │   │   │   │   │   │   ├── Csv.json
    │   │   │   │   │   │   │   ├── Csv.tsx
    │   │   │   │   │   │   │   ├── Doc.json
    │   │   │   │   │   │   │   ├── Doc.tsx
    │   │   │   │   │   │   │   ├── Docx.json
    │   │   │   │   │   │   │   ├── Docx.tsx
    │   │   │   │   │   │   │   ├── Html.json
    │   │   │   │   │   │   │   ├── Html.tsx
    │   │   │   │   │   │   │   ├── Json.json
    │   │   │   │   │   │   │   ├── Json.tsx
    │   │   │   │   │   │   │   ├── Md.json
    │   │   │   │   │   │   │   ├── Md.tsx
    │   │   │   │   │   │   │   ├── Pdf.json
    │   │   │   │   │   │   │   ├── Pdf.tsx
    │   │   │   │   │   │   │   ├── Txt.json
    │   │   │   │   │   │   │   ├── Txt.tsx
    │   │   │   │   │   │   │   ├── Unknow.json
    │   │   │   │   │   │   │   ├── Unknow.tsx
    │   │   │   │   │   │   │   ├── Xlsx.json
    │   │   │   │   │   │   │   ├── Xlsx.tsx
    │   │   │   │   │   │   │   ├── Yaml.json
    │   │   │   │   │   │   │   ├── Yaml.tsx
    │   │   │   │   │   │   │   └── index.ts
    │   │   │   │   │   │   ├── header-nav
    │   │   │   │   │   │   │   ├── explore
    │   │   │   │   │   │   │   │   ├── Explore.json
    │   │   │   │   │   │   │   │   ├── Explore.tsx
    │   │   │   │   │   │   │   │   ├── ExploreActive.json
    │   │   │   │   │   │   │   │   ├── ExploreActive.tsx
    │   │   │   │   │   │   │   │   └── index.ts
    │   │   │   │   │   │   │   ├── knowledge
    │   │   │   │   │   │   │   │   ├── Knowledge.json
    │   │   │   │   │   │   │   │   ├── Knowledge.tsx
    │   │   │   │   │   │   │   │   ├── KnowledgeActive.json
    │   │   │   │   │   │   │   │   ├── KnowledgeActive.tsx
    │   │   │   │   │   │   │   │   └── index.ts
    │   │   │   │   │   │   │   ├── studio
    │   │   │   │   │   │   │   │   ├── Robot.json
    │   │   │   │   │   │   │   │   ├── Robot.tsx
    │   │   │   │   │   │   │   │   ├── RobotActive.json
    │   │   │   │   │   │   │   │   ├── RobotActive.tsx
    │   │   │   │   │   │   │   │   └── index.ts
    │   │   │   │   │   │   │   └── tools
    │   │   │   │   │   │   │       ├── Tools.json
    │   │   │   │   │   │   │       ├── Tools.tsx
    │   │   │   │   │   │   │       ├── ToolsActive.json
    │   │   │   │   │   │   │       ├── ToolsActive.tsx
    │   │   │   │   │   │   │       └── index.ts
    │   │   │   │   │   │   ├── llm
    │   │   │   │   │   │   │   ├── Anthropic.json
    │   │   │   │   │   │   │   ├── Anthropic.tsx
    │   │   │   │   │   │   │   ├── AnthropicText.json
    │   │   │   │   │   │   │   ├── AnthropicText.tsx
    │   │   │   │   │   │   │   ├── AzureOpenaiService.json
    │   │   │   │   │   │   │   ├── AzureOpenaiService.tsx
    │   │   │   │   │   │   │   ├── AzureOpenaiServiceText.json
    │   │   │   │   │   │   │   ├── AzureOpenaiServiceText.tsx
    │   │   │   │   │   │   │   ├── Azureai.json
    │   │   │   │   │   │   │   ├── Azureai.tsx
    │   │   │   │   │   │   │   ├── AzureaiText.json
    │   │   │   │   │   │   │   ├── AzureaiText.tsx
    │   │   │   │   │   │   │   ├── Baichuan.json
    │   │   │   │   │   │   │   ├── Baichuan.tsx
    │   │   │   │   │   │   │   ├── BaichuanText.json
    │   │   │   │   │   │   │   ├── BaichuanText.tsx
    │   │   │   │   │   │   │   ├── Chatglm.json
    │   │   │   │   │   │   │   ├── Chatglm.tsx
    │   │   │   │   │   │   │   ├── ChatglmText.json
    │   │   │   │   │   │   │   ├── ChatglmText.tsx
    │   │   │   │   │   │   │   ├── Cohere.json
    │   │   │   │   │   │   │   ├── Cohere.tsx
    │   │   │   │   │   │   │   ├── CohereText.json
    │   │   │   │   │   │   │   ├── CohereText.tsx
    │   │   │   │   │   │   │   ├── Gpt3.json
    │   │   │   │   │   │   │   ├── Gpt3.tsx
    │   │   │   │   │   │   │   ├── Gpt4.json
    │   │   │   │   │   │   │   ├── Gpt4.tsx
    │   │   │   │   │   │   │   ├── Huggingface.json
    │   │   │   │   │   │   │   ├── Huggingface.tsx
    │   │   │   │   │   │   │   ├── HuggingfaceText.json
    │   │   │   │   │   │   │   ├── HuggingfaceText.tsx
    │   │   │   │   │   │   │   ├── HuggingfaceTextHub.json
    │   │   │   │   │   │   │   ├── HuggingfaceTextHub.tsx
    │   │   │   │   │   │   │   ├── IflytekSpark.json
    │   │   │   │   │   │   │   ├── IflytekSpark.tsx
    │   │   │   │   │   │   │   ├── IflytekSparkText.json
    │   │   │   │   │   │   │   ├── IflytekSparkText.tsx
    │   │   │   │   │   │   │   ├── IflytekSparkTextCn.json
    │   │   │   │   │   │   │   ├── IflytekSparkTextCn.tsx
    │   │   │   │   │   │   │   ├── Jina.json
    │   │   │   │   │   │   │   ├── Jina.tsx
    │   │   │   │   │   │   │   ├── JinaText.json
    │   │   │   │   │   │   │   ├── JinaText.tsx
    │   │   │   │   │   │   │   ├── Localai.json
    │   │   │   │   │   │   │   ├── Localai.tsx
    │   │   │   │   │   │   │   ├── LocalaiText.json
    │   │   │   │   │   │   │   ├── LocalaiText.tsx
    │   │   │   │   │   │   │   ├── Microsoft.json
    │   │   │   │   │   │   │   ├── Microsoft.tsx
    │   │   │   │   │   │   │   ├── OpenaiBlack.json
    │   │   │   │   │   │   │   ├── OpenaiBlack.tsx
    │   │   │   │   │   │   │   ├── OpenaiBlue.json
    │   │   │   │   │   │   │   ├── OpenaiBlue.tsx
    │   │   │   │   │   │   │   ├── OpenaiGreen.json
    │   │   │   │   │   │   │   ├── OpenaiGreen.tsx
    │   │   │   │   │   │   │   ├── OpenaiText.json
    │   │   │   │   │   │   │   ├── OpenaiText.tsx
    │   │   │   │   │   │   │   ├── OpenaiTransparent.json
    │   │   │   │   │   │   │   ├── OpenaiTransparent.tsx
    │   │   │   │   │   │   │   ├── OpenaiViolet.json
    │   │   │   │   │   │   │   ├── OpenaiViolet.tsx
    │   │   │   │   │   │   │   ├── Openllm.json
    │   │   │   │   │   │   │   ├── Openllm.tsx
    │   │   │   │   │   │   │   ├── OpenllmText.json
    │   │   │   │   │   │   │   ├── OpenllmText.tsx
    │   │   │   │   │   │   │   ├── Replicate.json
    │   │   │   │   │   │   │   ├── Replicate.tsx
    │   │   │   │   │   │   │   ├── ReplicateText.json
    │   │   │   │   │   │   │   ├── ReplicateText.tsx
    │   │   │   │   │   │   │   ├── XorbitsInference.json
    │   │   │   │   │   │   │   ├── XorbitsInference.tsx
    │   │   │   │   │   │   │   ├── XorbitsInferenceText.json
    │   │   │   │   │   │   │   ├── XorbitsInferenceText.tsx
    │   │   │   │   │   │   │   ├── Zhipuai.json
    │   │   │   │   │   │   │   ├── Zhipuai.tsx
    │   │   │   │   │   │   │   ├── ZhipuaiText.json
    │   │   │   │   │   │   │   ├── ZhipuaiText.tsx
    │   │   │   │   │   │   │   ├── ZhipuaiTextCn.json
    │   │   │   │   │   │   │   ├── ZhipuaiTextCn.tsx
    │   │   │   │   │   │   │   └── index.ts
    │   │   │   │   │   │   ├── model
    │   │   │   │   │   │   │   ├── Checked.json
    │   │   │   │   │   │   │   ├── Checked.tsx
    │   │   │   │   │   │   │   └── index.ts
    │   │   │   │   │   │   ├── other
    │   │   │   │   │   │   │   ├── DefaultToolIcon.json
    │   │   │   │   │   │   │   ├── DefaultToolIcon.tsx
    │   │   │   │   │   │   │   ├── Icon3Dots.json
    │   │   │   │   │   │   │   ├── Icon3Dots.tsx
    │   │   │   │   │   │   │   └── index.ts
    │   │   │   │   │   │   ├── plugins
    │   │   │   │   │   │   │   ├── Google.json
    │   │   │   │   │   │   │   ├── Google.tsx
    │   │   │   │   │   │   │   ├── WebReader.json
    │   │   │   │   │   │   │   ├── WebReader.tsx
    │   │   │   │   │   │   │   ├── Wikipedia.json
    │   │   │   │   │   │   │   ├── Wikipedia.tsx
    │   │   │   │   │   │   │   └── index.ts
    │   │   │   │   │   │   └── thought
    │   │   │   │   │   │       ├── DataSet.json
    │   │   │   │   │   │       ├── DataSet.tsx
    │   │   │   │   │   │       ├── Loading.json
    │   │   │   │   │   │       ├── Loading.tsx
    │   │   │   │   │   │       ├── Search.json
    │   │   │   │   │   │       ├── Search.tsx
    │   │   │   │   │   │       ├── ThoughtList.json
    │   │   │   │   │   │       ├── ThoughtList.tsx
    │   │   │   │   │   │       ├── WebReader.json
    │   │   │   │   │   │       ├── WebReader.tsx
    │   │   │   │   │   │       └── index.ts
    │   │   │   │   │   └── vender
    │   │   │   │   │       ├── line
    │   │   │   │   │       │   ├── alertsAndFeedback
    │   │   │   │   │       │   │   ├── AlertCircle.json
    │   │   │   │   │       │   │   ├── AlertCircle.tsx
    │   │   │   │   │       │   │   ├── AlertTriangle.json
    │   │   │   │   │       │   │   ├── AlertTriangle.tsx
    │   │   │   │   │       │   │   ├── ThumbsDown.json
    │   │   │   │   │       │   │   ├── ThumbsDown.tsx
    │   │   │   │   │       │   │   ├── ThumbsUp.json
    │   │   │   │   │       │   │   ├── ThumbsUp.tsx
    │   │   │   │   │       │   │   └── index.ts
    │   │   │   │   │       │   ├── arrows
    │   │   │   │   │       │   │   ├── ArrowNarrowLeft.json
    │   │   │   │   │       │   │   ├── ArrowNarrowLeft.tsx
    │   │   │   │   │       │   │   ├── ArrowNarrowRight.json
    │   │   │   │   │       │   │   ├── ArrowNarrowRight.tsx
    │   │   │   │   │       │   │   ├── ArrowUpRight.json
    │   │   │   │   │       │   │   ├── ArrowUpRight.tsx
    │   │   │   │   │       │   │   ├── ChevronDown.json
    │   │   │   │   │       │   │   ├── ChevronDown.tsx
    │   │   │   │   │       │   │   ├── ChevronDownDouble.json
    │   │   │   │   │       │   │   ├── ChevronDownDouble.tsx
    │   │   │   │   │       │   │   ├── ChevronRight.json
    │   │   │   │   │       │   │   ├── ChevronRight.tsx
    │   │   │   │   │       │   │   ├── ChevronSelectorVertical.json
    │   │   │   │   │       │   │   ├── ChevronSelectorVertical.tsx
    │   │   │   │   │       │   │   ├── Collapse04.json
    │   │   │   │   │       │   │   ├── Collapse04.tsx
    │   │   │   │   │       │   │   ├── FlipBackward.json
    │   │   │   │   │       │   │   ├── FlipBackward.tsx
    │   │   │   │   │       │   │   ├── FlipForward.json
    │   │   │   │   │       │   │   ├── FlipForward.tsx
    │   │   │   │   │       │   │   ├── RefreshCcw01.json
    │   │   │   │   │       │   │   ├── RefreshCcw01.tsx
    │   │   │   │   │       │   │   ├── RefreshCw05.json
    │   │   │   │   │       │   │   ├── RefreshCw05.tsx
    │   │   │   │   │       │   │   ├── ReverseLeft.json
    │   │   │   │   │       │   │   ├── ReverseLeft.tsx
    │   │   │   │   │       │   │   └── index.ts
    │   │   │   │   │       │   ├── communication
    │   │   │   │   │       │   │   ├── AiText.json
    │   │   │   │   │       │   │   ├── AiText.tsx
    │   │   │   │   │       │   │   ├── ChatBot.json
    │   │   │   │   │       │   │   ├── ChatBot.tsx
    │   │   │   │   │       │   │   ├── ChatBotSlim.json
    │   │   │   │   │       │   │   ├── ChatBotSlim.tsx
    │   │   │   │   │       │   │   ├── CuteRobot.json
    │   │   │   │   │       │   │   ├── CuteRobot.tsx
    │   │   │   │   │       │   │   ├── MessageCheckRemove.json
    │   │   │   │   │       │   │   ├── MessageCheckRemove.tsx
    │   │   │   │   │       │   │   ├── MessageFastPlus.json
    │   │   │   │   │       │   │   ├── MessageFastPlus.tsx
    │   │   │   │   │       │   │   ├── MessagePlay.json
    │   │   │   │   │       │   │   ├── MessagePlay.tsx
    │   │   │   │   │       │   │   └── index.ts
    │   │   │   │   │       │   ├── development
    │   │   │   │   │       │   │   ├── ArtificialBrain.json
    │   │   │   │   │       │   │   ├── ArtificialBrain.tsx
    │   │   │   │   │       │   │   ├── BarChartSquare02.json
    │   │   │   │   │       │   │   ├── BarChartSquare02.tsx
    │   │   │   │   │       │   │   ├── BracketsX.json
    │   │   │   │   │       │   │   ├── BracketsX.tsx
    │   │   │   │   │       │   │   ├── CodeBrowser.json
    │   │   │   │   │       │   │   ├── CodeBrowser.tsx
    │   │   │   │   │       │   │   ├── Container.json
    │   │   │   │   │       │   │   ├── Container.tsx
    │   │   │   │   │       │   │   ├── Database01.json
    │   │   │   │   │       │   │   ├── Database01.tsx
    │   │   │   │   │       │   │   ├── Database03.json
    │   │   │   │   │       │   │   ├── Database03.tsx
    │   │   │   │   │       │   │   ├── FileHeart02.json
    │   │   │   │   │       │   │   ├── FileHeart02.tsx
    │   │   │   │   │       │   │   ├── GitBranch01.json
    │   │   │   │   │       │   │   ├── GitBranch01.tsx
    │   │   │   │   │       │   │   ├── PromptEngineering.json
    │   │   │   │   │       │   │   ├── PromptEngineering.tsx
    │   │   │   │   │       │   │   ├── PuzzlePiece01.json
    │   │   │   │   │       │   │   ├── PuzzlePiece01.tsx
    │   │   │   │   │       │   │   ├── TerminalSquare.json
    │   │   │   │   │       │   │   ├── TerminalSquare.tsx
    │   │   │   │   │       │   │   ├── Variable.json
    │   │   │   │   │       │   │   ├── Variable.tsx
    │   │   │   │   │       │   │   ├── Webhooks.json
    │   │   │   │   │       │   │   ├── Webhooks.tsx
    │   │   │   │   │       │   │   └── index.ts
    │   │   │   │   │       │   ├── editor
    │   │   │   │   │       │   │   ├── AlignLeft.json
    │   │   │   │   │       │   │   ├── AlignLeft.tsx
    │   │   │   │   │       │   │   ├── BezierCurve03.json
    │   │   │   │   │       │   │   ├── BezierCurve03.tsx
    │   │   │   │   │       │   │   ├── Colors.json
    │   │   │   │   │       │   │   ├── Colors.tsx
    │   │   │   │   │       │   │   ├── Cursor02C.json
    │   │   │   │   │       │   │   ├── Cursor02C.tsx
    │   │   │   │   │       │   │   ├── Hand02.json
    │   │   │   │   │       │   │   ├── Hand02.tsx
    │   │   │   │   │       │   │   ├── ImageIndentLeft.json
    │   │   │   │   │       │   │   ├── ImageIndentLeft.tsx
    │   │   │   │   │       │   │   ├── LeftIndent02.json
    │   │   │   │   │       │   │   ├── LeftIndent02.tsx
    │   │   │   │   │       │   │   ├── LetterSpacing01.json
    │   │   │   │   │       │   │   ├── LetterSpacing01.tsx
    │   │   │   │   │       │   │   ├── TypeSquare.json
    │   │   │   │   │       │   │   ├── TypeSquare.tsx
    │   │   │   │   │       │   │   ├── ZoomIn.json
    │   │   │   │   │       │   │   ├── ZoomIn.tsx
    │   │   │   │   │       │   │   ├── ZoomOut.json
    │   │   │   │   │       │   │   ├── ZoomOut.tsx
    │   │   │   │   │       │   │   └── index.ts
    │   │   │   │   │       │   ├── education
    │   │   │   │   │       │   │   ├── BookOpen01.json
    │   │   │   │   │       │   │   ├── BookOpen01.tsx
    │   │   │   │   │       │   │   └── index.ts
    │   │   │   │   │       │   ├── files
    │   │   │   │   │       │   │   ├── Clipboard.json
    │   │   │   │   │       │   │   ├── Clipboard.tsx
    │   │   │   │   │       │   │   ├── ClipboardCheck.json
    │   │   │   │   │       │   │   ├── ClipboardCheck.tsx
    │   │   │   │   │       │   │   ├── File02.json
    │   │   │   │   │       │   │   ├── File02.tsx
    │   │   │   │   │       │   │   ├── FileArrow01.json
    │   │   │   │   │       │   │   ├── FileArrow01.tsx
    │   │   │   │   │       │   │   ├── FileCheck02.json
    │   │   │   │   │       │   │   ├── FileCheck02.tsx
    │   │   │   │   │       │   │   ├── FileDownload02.json
    │   │   │   │   │       │   │   ├── FileDownload02.tsx
    │   │   │   │   │       │   │   ├── FilePlus01.json
    │   │   │   │   │       │   │   ├── FilePlus01.tsx
    │   │   │   │   │       │   │   ├── FilePlus02.json
    │   │   │   │   │       │   │   ├── FilePlus02.tsx
    │   │   │   │   │       │   │   ├── FileText.json
    │   │   │   │   │       │   │   ├── FileText.tsx
    │   │   │   │   │       │   │   └── index.ts
    │   │   │   │   │       │   ├── financeAndECommerce
    │   │   │   │   │       │   │   ├── CoinsStacked01.json
    │   │   │   │   │       │   │   ├── CoinsStacked01.tsx
    │   │   │   │   │       │   │   ├── GoldCoin.json
    │   │   │   │   │       │   │   ├── GoldCoin.tsx
    │   │   │   │   │       │   │   ├── ReceiptList.json
    │   │   │   │   │       │   │   ├── ReceiptList.tsx
    │   │   │   │   │       │   │   ├── Tag01.json
    │   │   │   │   │       │   │   ├── Tag01.tsx
    │   │   │   │   │       │   │   ├── Tag03.json
    │   │   │   │   │       │   │   ├── Tag03.tsx
    │   │   │   │   │       │   │   └── index.ts
    │   │   │   │   │       │   ├── general
    │   │   │   │   │       │   │   ├── AtSign.json
    │   │   │   │   │       │   │   ├── AtSign.tsx
    │   │   │   │   │       │   │   ├── Bookmark.json
    │   │   │   │   │       │   │   ├── Bookmark.tsx
    │   │   │   │   │       │   │   ├── Check.json
    │   │   │   │   │       │   │   ├── Check.tsx
    │   │   │   │   │       │   │   ├── CheckCircle.json
    │   │   │   │   │       │   │   ├── CheckCircle.tsx
    │   │   │   │   │       │   │   ├── CheckDone01.json
    │   │   │   │   │       │   │   ├── CheckDone01.tsx
    │   │   │   │   │       │   │   ├── Checklist.json
    │   │   │   │   │       │   │   ├── Checklist.tsx
    │   │   │   │   │       │   │   ├── ChecklistSquare.json
    │   │   │   │   │       │   │   ├── ChecklistSquare.tsx
    │   │   │   │   │       │   │   ├── DotsGrid.json
    │   │   │   │   │       │   │   ├── DotsGrid.tsx
    │   │   │   │   │       │   │   ├── DotsHorizontal.json
    │   │   │   │   │       │   │   ├── DotsHorizontal.tsx
    │   │   │   │   │       │   │   ├── Edit02.json
    │   │   │   │   │       │   │   ├── Edit02.tsx
    │   │   │   │   │       │   │   ├── Edit03.json
    │   │   │   │   │       │   │   ├── Edit03.tsx
    │   │   │   │   │       │   │   ├── Edit04.json
    │   │   │   │   │       │   │   ├── Edit04.tsx
    │   │   │   │   │       │   │   ├── Edit05.json
    │   │   │   │   │       │   │   ├── Edit05.tsx
    │   │   │   │   │       │   │   ├── Hash02.json
    │   │   │   │   │       │   │   ├── Hash02.tsx
    │   │   │   │   │       │   │   ├── HelpCircle.json
    │   │   │   │   │       │   │   ├── HelpCircle.tsx
    │   │   │   │   │       │   │   ├── InfoCircle.json
    │   │   │   │   │       │   │   ├── InfoCircle.tsx
    │   │   │   │   │       │   │   ├── Link03.json
    │   │   │   │   │       │   │   ├── Link03.tsx
    │   │   │   │   │       │   │   ├── LinkExternal01.json
    │   │   │   │   │       │   │   ├── LinkExternal01.tsx
    │   │   │   │   │       │   │   ├── LinkExternal02.json
    │   │   │   │   │       │   │   ├── LinkExternal02.tsx
    │   │   │   │   │       │   │   ├── Loading02.json
    │   │   │   │   │       │   │   ├── Loading02.tsx
    │   │   │   │   │       │   │   ├── LogIn04.json
    │   │   │   │   │       │   │   ├── LogIn04.tsx
    │   │   │   │   │       │   │   ├── LogOut01.json
    │   │   │   │   │       │   │   ├── LogOut01.tsx
    │   │   │   │   │       │   │   ├── LogOut04.json
    │   │   │   │   │       │   │   ├── LogOut04.tsx
    │   │   │   │   │       │   │   ├── Menu01.json
    │   │   │   │   │       │   │   ├── Menu01.tsx
    │   │   │   │   │       │   │   ├── Pin01.json
    │   │   │   │   │       │   │   ├── Pin01.tsx
    │   │   │   │   │       │   │   ├── Pin02.json
    │   │   │   │   │       │   │   ├── Pin02.tsx
    │   │   │   │   │       │   │   ├── Plus.json
    │   │   │   │   │       │   │   ├── Plus.tsx
    │   │   │   │   │       │   │   ├── Plus02.json
    │   │   │   │   │       │   │   ├── Plus02.tsx
    │   │   │   │   │       │   │   ├── SearchLg.json
    │   │   │   │   │       │   │   ├── SearchLg.tsx
    │   │   │   │   │       │   │   ├── Settings01.json
    │   │   │   │   │       │   │   ├── Settings01.tsx
    │   │   │   │   │       │   │   ├── Settings04.json
    │   │   │   │   │       │   │   ├── Settings04.tsx
    │   │   │   │   │       │   │   ├── Target04.json
    │   │   │   │   │       │   │   ├── Target04.tsx
    │   │   │   │   │       │   │   ├── Trash03.json
    │   │   │   │   │       │   │   ├── Trash03.tsx
    │   │   │   │   │       │   │   ├── Upload03.json
    │   │   │   │   │       │   │   ├── Upload03.tsx
    │   │   │   │   │       │   │   ├── UploadCloud01.json
    │   │   │   │   │       │   │   ├── UploadCloud01.tsx
    │   │   │   │   │       │   │   ├── X.json
    │   │   │   │   │       │   │   ├── X.tsx
    │   │   │   │   │       │   │   ├── XClose.json
    │   │   │   │   │       │   │   ├── XClose.tsx
    │   │   │   │   │       │   │   └── index.ts
    │   │   │   │   │       │   ├── images
    │   │   │   │   │       │   │   ├── ImagePlus.json
    │   │   │   │   │       │   │   ├── ImagePlus.tsx
    │   │   │   │   │       │   │   └── index.ts
    │   │   │   │   │       │   ├── layout
    │   │   │   │   │       │   │   ├── AlignLeft01.json
    │   │   │   │   │       │   │   ├── AlignLeft01.tsx
    │   │   │   │   │       │   │   ├── AlignRight01.json
    │   │   │   │   │       │   │   ├── AlignRight01.tsx
    │   │   │   │   │       │   │   ├── Grid01.json
    │   │   │   │   │       │   │   ├── Grid01.tsx
    │   │   │   │   │       │   │   ├── LayoutGrid02.json
    │   │   │   │   │       │   │   ├── LayoutGrid02.tsx
    │   │   │   │   │       │   │   ├── OrganizeGrid.json
    │   │   │   │   │       │   │   ├── OrganizeGrid.tsx
    │   │   │   │   │       │   │   └── index.ts
    │   │   │   │   │       │   ├── mapsAndTravel
    │   │   │   │   │       │   │   ├── Globe01.json
    │   │   │   │   │       │   │   ├── Globe01.tsx
    │   │   │   │   │       │   │   ├── Route.json
    │   │   │   │   │       │   │   ├── Route.tsx
    │   │   │   │   │       │   │   └── index.ts
    │   │   │   │   │       │   ├── mediaAndDevices
    │   │   │   │   │       │   │   ├── Microphone01.json
    │   │   │   │   │       │   │   ├── Microphone01.tsx
    │   │   │   │   │       │   │   ├── Play.json
    │   │   │   │   │       │   │   ├── Play.tsx
    │   │   │   │   │       │   │   ├── PlayCircle.json
    │   │   │   │   │       │   │   ├── PlayCircle.tsx
    │   │   │   │   │       │   │   ├── SlidersH.json
    │   │   │   │   │       │   │   ├── SlidersH.tsx
    │   │   │   │   │       │   │   ├── Speaker.json
    │   │   │   │   │       │   │   ├── Speaker.tsx
    │   │   │   │   │       │   │   ├── Stop.json
    │   │   │   │   │       │   │   ├── Stop.tsx
    │   │   │   │   │       │   │   ├── StopCircle.json
    │   │   │   │   │       │   │   ├── StopCircle.tsx
    │   │   │   │   │       │   │   └── index.ts
    │   │   │   │   │       │   ├── others
    │   │   │   │   │       │   │   ├── DragHandle.json
    │   │   │   │   │       │   │   ├── DragHandle.tsx
    │   │   │   │   │       │   │   └── index.ts
    │   │   │   │   │       │   ├── shapes
    │   │   │   │   │       │   │   ├── CubeOutline.json
    │   │   │   │   │       │   │   ├── CubeOutline.tsx
    │   │   │   │   │       │   │   └── index.ts
    │   │   │   │   │       │   ├── time
    │   │   │   │   │       │   │   ├── ClockFastForward.json
    │   │   │   │   │       │   │   ├── ClockFastForward.tsx
    │   │   │   │   │       │   │   ├── ClockPlay.json
    │   │   │   │   │       │   │   ├── ClockPlay.tsx
    │   │   │   │   │       │   │   ├── ClockPlaySlim.json
    │   │   │   │   │       │   │   ├── ClockPlaySlim.tsx
    │   │   │   │   │       │   │   ├── ClockRefresh.json
    │   │   │   │   │       │   │   ├── ClockRefresh.tsx
    │   │   │   │   │       │   │   └── index.ts
    │   │   │   │   │       │   ├── users
    │   │   │   │   │       │   │   ├── User01.json
    │   │   │   │   │       │   │   ├── User01.tsx
    │   │   │   │   │       │   │   ├── Users01.json
    │   │   │   │   │       │   │   ├── Users01.tsx
    │   │   │   │   │       │   │   └── index.ts
    │   │   │   │   │       │   └── weather
    │   │   │   │   │       │       ├── Stars02.json
    │   │   │   │   │       │       ├── Stars02.tsx
    │   │   │   │   │       │       └── index.ts
    │   │   │   │   │       ├── solid
    │   │   │   │   │       │   ├── FinanceAndECommerce
    │   │   │   │   │       │   │   ├── GoldCoin.json
    │   │   │   │   │       │   │   ├── GoldCoin.tsx
    │   │   │   │   │       │   │   ├── Scales02.json
    │   │   │   │   │       │   │   ├── Scales02.tsx
    │   │   │   │   │       │   │   └── index.ts
    │   │   │   │   │       │   ├── alertsAndFeedback
    │   │   │   │   │       │   │   ├── AlertCircle.json
    │   │   │   │   │       │   │   ├── AlertCircle.tsx
    │   │   │   │   │       │   │   ├── AlertTriangle.json
    │   │   │   │   │       │   │   ├── AlertTriangle.tsx
    │   │   │   │   │       │   │   └── index.ts
    │   │   │   │   │       │   ├── arrows
    │   │   │   │   │       │   │   ├── ChevronDown.json
    │   │   │   │   │       │   │   ├── ChevronDown.tsx
    │   │   │   │   │       │   │   ├── Expand04.json
    │   │   │   │   │       │   │   ├── Expand04.tsx
    │   │   │   │   │       │   │   ├── HighPriority.json
    │   │   │   │   │       │   │   ├── HighPriority.tsx
    │   │   │   │   │       │   │   └── index.ts
    │   │   │   │   │       │   ├── communication
    │   │   │   │   │       │   │   ├── AiText.json
    │   │   │   │   │       │   │   ├── AiText.tsx
    │   │   │   │   │       │   │   ├── ChatBot.json
    │   │   │   │   │       │   │   ├── ChatBot.tsx
    │   │   │   │   │       │   │   ├── CuteRobote.json
    │   │   │   │   │       │   │   ├── CuteRobote.tsx
    │   │   │   │   │       │   │   ├── EditList.json
    │   │   │   │   │       │   │   ├── EditList.tsx
    │   │   │   │   │       │   │   ├── MessageDotsCircle.json
    │   │   │   │   │       │   │   ├── MessageDotsCircle.tsx
    │   │   │   │   │       │   │   ├── MessageFast.json
    │   │   │   │   │       │   │   ├── MessageFast.tsx
    │   │   │   │   │       │   │   ├── MessageHeartCircle.json
    │   │   │   │   │       │   │   ├── MessageHeartCircle.tsx
    │   │   │   │   │       │   │   ├── MessageSmileSquare.json
    │   │   │   │   │       │   │   ├── MessageSmileSquare.tsx
    │   │   │   │   │       │   │   ├── Send03.json
    │   │   │   │   │       │   │   ├── Send03.tsx
    │   │   │   │   │       │   │   └── index.ts
    │   │   │   │   │       │   ├── development
    │   │   │   │   │       │   │   ├── ApiConnection.json
    │   │   │   │   │       │   │   ├── ApiConnection.tsx
    │   │   │   │   │       │   │   ├── BarChartSquare02.json
    │   │   │   │   │       │   │   ├── BarChartSquare02.tsx
    │   │   │   │   │       │   │   ├── Container.json
    │   │   │   │   │       │   │   ├── Container.tsx
    │   │   │   │   │       │   │   ├── Database02.json
    │   │   │   │   │       │   │   ├── Database02.tsx
    │   │   │   │   │       │   │   ├── Database03.json
    │   │   │   │   │       │   │   ├── Database03.tsx
    │   │   │   │   │       │   │   ├── FileHeart02.json
    │   │   │   │   │       │   │   ├── FileHeart02.tsx
    │   │   │   │   │       │   │   ├── PatternRecognition.json
    │   │   │   │   │       │   │   ├── PatternRecognition.tsx
    │   │   │   │   │       │   │   ├── PromptEngineering.json
    │   │   │   │   │       │   │   ├── PromptEngineering.tsx
    │   │   │   │   │       │   │   ├── PuzzlePiece01.json
    │   │   │   │   │       │   │   ├── PuzzlePiece01.tsx
    │   │   │   │   │       │   │   ├── Semantic.json
    │   │   │   │   │       │   │   ├── Semantic.tsx
    │   │   │   │   │       │   │   ├── TerminalSquare.json
    │   │   │   │   │       │   │   ├── TerminalSquare.tsx
    │   │   │   │   │       │   │   ├── Variable02.json
    │   │   │   │   │       │   │   ├── Variable02.tsx
    │   │   │   │   │       │   │   └── index.ts
    │   │   │   │   │       │   ├── editor
    │   │   │   │   │       │   │   ├── Brush01.json
    │   │   │   │   │       │   │   ├── Brush01.tsx
    │   │   │   │   │       │   │   ├── Citations.json
    │   │   │   │   │       │   │   ├── Citations.tsx
    │   │   │   │   │       │   │   ├── Colors.json
    │   │   │   │   │       │   │   ├── Colors.tsx
    │   │   │   │   │       │   │   ├── Cursor02C.json
    │   │   │   │   │       │   │   ├── Cursor02C.tsx
    │   │   │   │   │       │   │   ├── Hand02.json
    │   │   │   │   │       │   │   ├── Hand02.tsx
    │   │   │   │   │       │   │   ├── Paragraph.json
    │   │   │   │   │       │   │   ├── Paragraph.tsx
    │   │   │   │   │       │   │   ├── TypeSquare.json
    │   │   │   │   │       │   │   ├── TypeSquare.tsx
    │   │   │   │   │       │   │   └── index.ts
    │   │   │   │   │       │   ├── education
    │   │   │   │   │       │   │   ├── Beaker02.json
    │   │   │   │   │       │   │   ├── Beaker02.tsx
    │   │   │   │   │       │   │   ├── BubbleText.json
    │   │   │   │   │       │   │   ├── BubbleText.tsx
    │   │   │   │   │       │   │   ├── Heart02.json
    │   │   │   │   │       │   │   ├── Heart02.tsx
    │   │   │   │   │       │   │   ├── Unblur.json
    │   │   │   │   │       │   │   ├── Unblur.tsx
    │   │   │   │   │       │   │   └── index.ts
    │   │   │   │   │       │   ├── files
    │   │   │   │   │       │   │   ├── File05.json
    │   │   │   │   │       │   │   ├── File05.tsx
    │   │   │   │   │       │   │   ├── FileSearch02.json
    │   │   │   │   │       │   │   ├── FileSearch02.tsx
    │   │   │   │   │       │   │   ├── Folder.json
    │   │   │   │   │       │   │   ├── Folder.tsx
    │   │   │   │   │       │   │   └── index.ts
    │   │   │   │   │       │   ├── general
    │   │   │   │   │       │   │   ├── AnswerTriangle.json
    │   │   │   │   │       │   │   ├── AnswerTriangle.tsx
    │   │   │   │   │       │   │   ├── CheckCircle.json
    │   │   │   │   │       │   │   ├── CheckCircle.tsx
    │   │   │   │   │       │   │   ├── CheckDone01.json
    │   │   │   │   │       │   │   ├── CheckDone01.tsx
    │   │   │   │   │       │   │   ├── Download02.json
    │   │   │   │   │       │   │   ├── Download02.tsx
    │   │   │   │   │       │   │   ├── Edit03.json
    │   │   │   │   │       │   │   ├── Edit03.tsx
    │   │   │   │   │       │   │   ├── Edit04.json
    │   │   │   │   │       │   │   ├── Edit04.tsx
    │   │   │   │   │       │   │   ├── Eye.json
    │   │   │   │   │       │   │   ├── Eye.tsx
    │   │   │   │   │       │   │   ├── MessageClockCircle.json
    │   │   │   │   │       │   │   ├── MessageClockCircle.tsx
    │   │   │   │   │       │   │   ├── PlusCircle.json
    │   │   │   │   │       │   │   ├── PlusCircle.tsx
    │   │   │   │   │       │   │   ├── QuestionTriangle.json
    │   │   │   │   │       │   │   ├── QuestionTriangle.tsx
    │   │   │   │   │       │   │   ├── SearchMd.json
    │   │   │   │   │       │   │   ├── SearchMd.tsx
    │   │   │   │   │       │   │   ├── Target04.json
    │   │   │   │   │       │   │   ├── Target04.tsx
    │   │   │   │   │       │   │   ├── Tool03.json
    │   │   │   │   │       │   │   ├── Tool03.tsx
    │   │   │   │   │       │   │   ├── XCircle.json
    │   │   │   │   │       │   │   ├── XCircle.tsx
    │   │   │   │   │       │   │   ├── ZapFast.json
    │   │   │   │   │       │   │   ├── ZapFast.tsx
    │   │   │   │   │       │   │   ├── ZapNarrow.json
    │   │   │   │   │       │   │   ├── ZapNarrow.tsx
    │   │   │   │   │       │   │   └── index.ts
    │   │   │   │   │       │   ├── layout
    │   │   │   │   │       │   │   ├── Grid01.json
    │   │   │   │   │       │   │   ├── Grid01.tsx
    │   │   │   │   │       │   │   └── index.ts
    │   │   │   │   │       │   ├── mapsAndTravel
    │   │   │   │   │       │   │   ├── Route.json
    │   │   │   │   │       │   │   ├── Route.tsx
    │   │   │   │   │       │   │   └── index.ts
    │   │   │   │   │       │   ├── mediaAndDevices
    │   │   │   │   │       │   │   ├── MagicBox.json
    │   │   │   │   │       │   │   ├── MagicBox.tsx
    │   │   │   │   │       │   │   ├── MagicEyes.json
    │   │   │   │   │       │   │   ├── MagicEyes.tsx
    │   │   │   │   │       │   │   ├── MagicWand.json
    │   │   │   │   │       │   │   ├── MagicWand.tsx
    │   │   │   │   │       │   │   ├── Microphone01.json
    │   │   │   │   │       │   │   ├── Microphone01.tsx
    │   │   │   │   │       │   │   ├── Play.json
    │   │   │   │   │       │   │   ├── Play.tsx
    │   │   │   │   │       │   │   ├── Robot.json
    │   │   │   │   │       │   │   ├── Robot.tsx
    │   │   │   │   │       │   │   ├── Sliders02.json
    │   │   │   │   │       │   │   ├── Sliders02.tsx
    │   │   │   │   │       │   │   ├── Speaker.json
    │   │   │   │   │       │   │   ├── Speaker.tsx
    │   │   │   │   │       │   │   ├── StopCircle.json
    │   │   │   │   │       │   │   ├── StopCircle.tsx
    │   │   │   │   │       │   │   └── index.ts
    │   │   │   │   │       │   ├── security
    │   │   │   │   │       │   │   ├── Lock01.json
    │   │   │   │   │       │   │   ├── Lock01.tsx
    │   │   │   │   │       │   │   └── index.ts
    │   │   │   │   │       │   ├── shapes
    │   │   │   │   │       │   │   ├── Star04.json
    │   │   │   │   │       │   │   ├── Star04.tsx
    │   │   │   │   │       │   │   ├── Star06.json
    │   │   │   │   │       │   │   ├── Star06.tsx
    │   │   │   │   │       │   │   └── index.ts
    │   │   │   │   │       │   └── users
    │   │   │   │   │       │       ├── User01.json
    │   │   │   │   │       │       ├── User01.tsx
    │   │   │   │   │       │       ├── UserEdit02.json
    │   │   │   │   │       │       ├── UserEdit02.tsx
    │   │   │   │   │       │       ├── Users01.json
    │   │   │   │   │       │       ├── Users01.tsx
    │   │   │   │   │       │       └── index.ts
    │   │   │   │   │       └── workflow
    │   │   │   │   │           ├── Answer.json
    │   │   │   │   │           ├── Answer.tsx
    │   │   │   │   │           ├── Code.json
    │   │   │   │   │           ├── Code.tsx
    │   │   │   │   │           ├── End.json
    │   │   │   │   │           ├── End.tsx
    │   │   │   │   │           ├── Home.json
    │   │   │   │   │           ├── Home.tsx
    │   │   │   │   │           ├── Http.json
    │   │   │   │   │           ├── Http.tsx
    │   │   │   │   │           ├── IfElse.json
    │   │   │   │   │           ├── IfElse.tsx
    │   │   │   │   │           ├── Jinja.json
    │   │   │   │   │           ├── Jinja.tsx
    │   │   │   │   │           ├── KnowledgeRetrieval.json
    │   │   │   │   │           ├── KnowledgeRetrieval.tsx
    │   │   │   │   │           ├── Llm.json
    │   │   │   │   │           ├── Llm.tsx
    │   │   │   │   │           ├── QuestionClassifier.json
    │   │   │   │   │           ├── QuestionClassifier.tsx
    │   │   │   │   │           ├── TemplatingTransform.json
    │   │   │   │   │           ├── TemplatingTransform.tsx
    │   │   │   │   │           ├── VariableX.json
    │   │   │   │   │           ├── VariableX.tsx
    │   │   │   │   │           └── index.ts
    │   │   │   │   └── utils.ts
    │   │   │   ├── image-gallery
    │   │   │   │   ├── index.tsx
    │   │   │   │   └── style.module.css
    │   │   │   ├── image-uploader
    │   │   │   │   ├── chat-image-uploader.tsx
    │   │   │   │   ├── hooks.ts
    │   │   │   │   ├── image-link-input.tsx
    │   │   │   │   ├── image-list.tsx
    │   │   │   │   ├── image-preview.tsx
    │   │   │   │   ├── text-generation-image-uploader.tsx
    │   │   │   │   ├── uploader.tsx
    │   │   │   │   └── utils.ts
    │   │   │   ├── input
    │   │   │   │   ├── index.tsx
    │   │   │   │   └── style.module.css
    │   │   │   ├── loading
    │   │   │   │   ├── index.tsx
    │   │   │   │   └── style.css
    │   │   │   ├── logo
    │   │   │   │   ├── logo-embeded-chat-avatar.tsx
    │   │   │   │   ├── logo-embeded-chat-header.tsx
    │   │   │   │   └── logo-site.tsx
    │   │   │   ├── markdown.tsx
    │   │   │   ├── message-log-modal
    │   │   │   │   └── index.tsx
    │   │   │   ├── modal
    │   │   │   │   ├── delete-confirm-modal
    │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   └── style.module.css
    │   │   │   │   └── index.tsx
    │   │   │   ├── notion-icon
    │   │   │   │   ├── index.module.css
    │   │   │   │   └── index.tsx
    │   │   │   ├── notion-page-selector
    │   │   │   │   ├── assets
    │   │   │   │   │   ├── clear.svg
    │   │   │   │   │   ├── down-arrow.svg
    │   │   │   │   │   ├── notion-empty-page.svg
    │   │   │   │   │   ├── notion-page.svg
    │   │   │   │   │   ├── search.svg
    │   │   │   │   │   └── setting.svg
    │   │   │   │   ├── base.module.css
    │   │   │   │   ├── base.tsx
    │   │   │   │   ├── index.tsx
    │   │   │   │   ├── notion-page-selector-modal
    │   │   │   │   │   ├── index.module.css
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── page-selector
    │   │   │   │   │   ├── index.module.css
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── search-input
    │   │   │   │   │   ├── index.module.css
    │   │   │   │   │   └── index.tsx
    │   │   │   │   └── workspace-selector
    │   │   │   │       ├── index.module.css
    │   │   │   │       └── index.tsx
    │   │   │   ├── pagination
    │   │   │   │   ├── index.tsx
    │   │   │   │   └── style.module.css
    │   │   │   ├── panel
    │   │   │   │   └── index.tsx
    │   │   │   ├── param-item
    │   │   │   │   ├── index.tsx
    │   │   │   │   ├── score-threshold-item.tsx
    │   │   │   │   └── top-k-item.tsx
    │   │   │   ├── popover
    │   │   │   │   ├── index.tsx
    │   │   │   │   └── style.module.css
    │   │   │   ├── portal-to-follow-elem
    │   │   │   │   └── index.tsx
    │   │   │   ├── progress-bar
    │   │   │   │   └── index.tsx
    │   │   │   ├── prompt-editor
    │   │   │   │   ├── constants.tsx
    │   │   │   │   ├── hooks.ts
    │   │   │   │   ├── index.tsx
    │   │   │   │   ├── plugins
    │   │   │   │   │   ├── component-picker-block
    │   │   │   │   │   │   ├── external-tool-option.tsx
    │   │   │   │   │   │   ├── hooks.tsx
    │   │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   │   ├── prompt-menu.tsx
    │   │   │   │   │   │   ├── prompt-option.tsx
    │   │   │   │   │   │   ├── variable-menu.tsx
    │   │   │   │   │   │   └── variable-option.tsx
    │   │   │   │   │   ├── context-block
    │   │   │   │   │   │   ├── component.tsx
    │   │   │   │   │   │   ├── context-block-replacement-block.tsx
    │   │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   │   └── node.tsx
    │   │   │   │   │   ├── custom-text
    │   │   │   │   │   │   └── node.tsx
    │   │   │   │   │   ├── history-block
    │   │   │   │   │   │   ├── component.tsx
    │   │   │   │   │   │   ├── history-block-replacement-block.tsx
    │   │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   │   └── node.tsx
    │   │   │   │   │   ├── on-blur-or-focus-block.tsx
    │   │   │   │   │   ├── placeholder.tsx
    │   │   │   │   │   ├── query-block
    │   │   │   │   │   │   ├── component.tsx
    │   │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   │   ├── node.tsx
    │   │   │   │   │   │   └── query-block-replacement-block.tsx
    │   │   │   │   │   ├── tree-view.tsx
    │   │   │   │   │   ├── update-block.tsx
    │   │   │   │   │   ├── variable-block
    │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   ├── variable-value-block
    │   │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   │   ├── node.tsx
    │   │   │   │   │   │   └── utils.ts
    │   │   │   │   │   └── workflow-variable-block
    │   │   │   │   │       ├── component.tsx
    │   │   │   │   │       ├── index.tsx
    │   │   │   │   │       ├── node.tsx
    │   │   │   │   │       └── workflow-variable-block-replacement-block.tsx
    │   │   │   │   ├── types.ts
    │   │   │   │   └── utils.ts
    │   │   │   ├── prompt-log-modal
    │   │   │   │   ├── card.tsx
    │   │   │   │   └── index.tsx
    │   │   │   ├── qrcode
    │   │   │   │   ├── index.tsx
    │   │   │   │   └── style.module.css
    │   │   │   ├── radio
    │   │   │   │   ├── component
    │   │   │   │   │   ├── group
    │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   └── radio
    │   │   │   │   │       └── index.tsx
    │   │   │   │   ├── context
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── index.tsx
    │   │   │   │   ├── style.module.css
    │   │   │   │   └── ui.tsx
    │   │   │   ├── radio-card
    │   │   │   │   ├── index.tsx
    │   │   │   │   ├── simple
    │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   └── style.module.css
    │   │   │   │   └── style.module.css
    │   │   │   ├── retry-button
    │   │   │   │   ├── index.tsx
    │   │   │   │   └── style.module.css
    │   │   │   ├── search-input
    │   │   │   │   └── index.tsx
    │   │   │   ├── select
    │   │   │   │   ├── index.tsx
    │   │   │   │   └── locale.tsx
    │   │   │   ├── slider
    │   │   │   │   ├── index.tsx
    │   │   │   │   └── style.css
    │   │   │   ├── spinner
    │   │   │   │   └── index.tsx
    │   │   │   ├── switch
    │   │   │   │   └── index.tsx
    │   │   │   ├── tab-header
    │   │   │   │   ├── index.tsx
    │   │   │   │   └── style.module.css
    │   │   │   ├── tab-slider
    │   │   │   │   └── index.tsx
    │   │   │   ├── tab-slider-new
    │   │   │   │   └── index.tsx
    │   │   │   ├── tab-slider-plain
    │   │   │   │   └── index.tsx
    │   │   │   ├── tag
    │   │   │   │   └── index.tsx
    │   │   │   ├── tag-input
    │   │   │   │   └── index.tsx
    │   │   │   ├── tag-management
    │   │   │   │   ├── constant.ts
    │   │   │   │   ├── filter.tsx
    │   │   │   │   ├── index.tsx
    │   │   │   │   ├── selector.tsx
    │   │   │   │   ├── store.ts
    │   │   │   │   ├── style.module.css
    │   │   │   │   ├── tag-item-editor.tsx
    │   │   │   │   └── tag-remove-modal.tsx
    │   │   │   ├── text-generation
    │   │   │   │   ├── hooks.ts
    │   │   │   │   └── types.ts
    │   │   │   ├── toast
    │   │   │   │   ├── index.tsx
    │   │   │   │   └── style.module.css
    │   │   │   ├── tooltip
    │   │   │   │   └── index.tsx
    │   │   │   ├── tooltip-plus
    │   │   │   │   └── index.tsx
    │   │   │   ├── topbar
    │   │   │   │   └── index.tsx
    │   │   │   └── voice-input
    │   │   │       ├── index.module.css
    │   │   │       ├── index.tsx
    │   │   │       └── utils.ts
    │   │   ├── billing
    │   │   │   ├── annotation-full
    │   │   │   │   ├── index.tsx
    │   │   │   │   ├── modal.tsx
    │   │   │   │   ├── style.module.css
    │   │   │   │   └── usage.tsx
    │   │   │   ├── apps-full
    │   │   │   │   ├── index.tsx
    │   │   │   │   └── style.module.css
    │   │   │   ├── apps-full-in-dialog
    │   │   │   │   ├── index.tsx
    │   │   │   │   └── style.module.css
    │   │   │   ├── billing-page
    │   │   │   │   └── index.tsx
    │   │   │   ├── config.ts
    │   │   │   ├── header-billing-btn
    │   │   │   │   └── index.tsx
    │   │   │   ├── plan
    │   │   │   │   └── index.tsx
    │   │   │   ├── pricing
    │   │   │   │   ├── index.tsx
    │   │   │   │   ├── plan-item.tsx
    │   │   │   │   └── select-plan-range.tsx
    │   │   │   ├── priority-label
    │   │   │   │   └── index.tsx
    │   │   │   ├── progress-bar
    │   │   │   │   └── index.tsx
    │   │   │   ├── type.ts
    │   │   │   ├── upgrade-btn
    │   │   │   │   ├── index.tsx
    │   │   │   │   └── style.module.css
    │   │   │   ├── usage-info
    │   │   │   │   ├── apps-info.tsx
    │   │   │   │   ├── index.tsx
    │   │   │   │   └── vector-space-info.tsx
    │   │   │   ├── utils
    │   │   │   │   └── index.ts
    │   │   │   └── vector-space-full
    │   │   │       ├── index.tsx
    │   │   │       └── style.module.css
    │   │   ├── browser-initor.tsx
    │   │   ├── custom
    │   │   │   ├── custom-app-header-brand
    │   │   │   │   ├── index.tsx
    │   │   │   │   └── style.module.css
    │   │   │   ├── custom-page
    │   │   │   │   └── index.tsx
    │   │   │   ├── custom-web-app-brand
    │   │   │   │   ├── index.tsx
    │   │   │   │   └── style.module.css
    │   │   │   └── style.module.css
    │   │   ├── datasets
    │   │   │   ├── api
    │   │   │   │   └── index.tsx
    │   │   │   ├── common
    │   │   │   │   ├── check-rerank-model.ts
    │   │   │   │   ├── economical-retrieval-method-config
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── retrieval-method-config
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── retrieval-method-info
    │   │   │   │   │   └── index.tsx
    │   │   │   │   └── retrieval-param-config
    │   │   │   │       └── index.tsx
    │   │   │   ├── create
    │   │   │   │   ├── assets
    │   │   │   │   │   ├── Icon-3-dots.svg
    │   │   │   │   │   ├── Loading.svg
    │   │   │   │   │   ├── alert-triangle.svg
    │   │   │   │   │   ├── annotation-info.svg
    │   │   │   │   │   ├── arrow-narrow-left.svg
    │   │   │   │   │   ├── book-open-01.svg
    │   │   │   │   │   ├── check.svg
    │   │   │   │   │   ├── close.svg
    │   │   │   │   │   ├── csv.svg
    │   │   │   │   │   ├── doc.svg
    │   │   │   │   │   ├── docx.svg
    │   │   │   │   │   ├── file.svg
    │   │   │   │   │   ├── folder-plus.svg
    │   │   │   │   │   ├── html.svg
    │   │   │   │   │   ├── json.svg
    │   │   │   │   │   ├── md.svg
    │   │   │   │   │   ├── normal.svg
    │   │   │   │   │   ├── notion.svg
    │   │   │   │   │   ├── pdf.svg
    │   │   │   │   │   ├── piggy-bank-01.svg
    │   │   │   │   │   ├── sliders-02.svg
    │   │   │   │   │   ├── star-07.svg
    │   │   │   │   │   ├── star.svg
    │   │   │   │   │   ├── trash.svg
    │   │   │   │   │   ├── txt.svg
    │   │   │   │   │   ├── unknow.svg
    │   │   │   │   │   ├── upload-cloud-01.svg
    │   │   │   │   │   ├── web.svg
    │   │   │   │   │   ├── xlsx.svg
    │   │   │   │   │   └── zap-fast.svg
    │   │   │   │   ├── embedding-process
    │   │   │   │   │   ├── index.module.css
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── empty-dataset-creation-modal
    │   │   │   │   │   ├── index.module.css
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── file-preview
    │   │   │   │   │   ├── index.module.css
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── file-uploader
    │   │   │   │   │   ├── index.module.css
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── index.module.css
    │   │   │   │   ├── index.tsx
    │   │   │   │   ├── notion-page-preview
    │   │   │   │   │   ├── index.module.css
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── step-one
    │   │   │   │   │   ├── index.module.css
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── step-three
    │   │   │   │   │   ├── index.module.css
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── step-two
    │   │   │   │   │   ├── index.module.css
    │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   ├── language-select
    │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   └── preview-item
    │   │   │   │   │       └── index.tsx
    │   │   │   │   ├── steps-nav-bar
    │   │   │   │   │   ├── index.module.css
    │   │   │   │   │   └── index.tsx
    │   │   │   │   └── stop-embedding-modal
    │   │   │   │       ├── index.module.css
    │   │   │   │       └── index.tsx
    │   │   │   ├── documents
    │   │   │   │   ├── assets
    │   │   │   │   │   ├── atSign.svg
    │   │   │   │   │   ├── bezierCurve.svg
    │   │   │   │   │   ├── bookOpen.svg
    │   │   │   │   │   ├── briefcase.svg
    │   │   │   │   │   ├── cardLoading.svg
    │   │   │   │   │   ├── file.svg
    │   │   │   │   │   ├── globe.svg
    │   │   │   │   │   ├── graduationHat.svg
    │   │   │   │   │   ├── hitLoading.svg
    │   │   │   │   │   ├── layoutRightClose.svg
    │   │   │   │   │   ├── layoutRightShow.svg
    │   │   │   │   │   ├── messageTextCircle.svg
    │   │   │   │   │   ├── normal.svg
    │   │   │   │   │   ├── star.svg
    │   │   │   │   │   ├── target.svg
    │   │   │   │   │   └── typeSquare.svg
    │   │   │   │   ├── detail
    │   │   │   │   │   ├── batch-modal
    │   │   │   │   │   │   ├── csv-downloader.tsx
    │   │   │   │   │   │   ├── csv-uploader.tsx
    │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   ├── completed
    │   │   │   │   │   │   ├── InfiniteVirtualList.tsx
    │   │   │   │   │   │   ├── SegmentCard.tsx
    │   │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   │   └── style.module.css
    │   │   │   │   │   ├── embedding
    │   │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   │   └── style.module.css
    │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   ├── metadata
    │   │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   │   └── style.module.css
    │   │   │   │   │   ├── new-segment-modal.tsx
    │   │   │   │   │   ├── segment-add
    │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   ├── settings
    │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   └── style.module.css
    │   │   │   │   ├── index.tsx
    │   │   │   │   ├── list.tsx
    │   │   │   │   └── style.module.css
    │   │   │   ├── hit-testing
    │   │   │   │   ├── assets
    │   │   │   │   │   ├── clock.svg
    │   │   │   │   │   ├── grid.svg
    │   │   │   │   │   └── plugin.svg
    │   │   │   │   ├── hit-detail.tsx
    │   │   │   │   ├── index.tsx
    │   │   │   │   ├── modify-retrieval-modal.tsx
    │   │   │   │   ├── style.module.css
    │   │   │   │   └── textarea.tsx
    │   │   │   ├── rename-modal
    │   │   │   │   └── index.tsx
    │   │   │   └── settings
    │   │   │       ├── form
    │   │   │       │   └── index.tsx
    │   │   │       ├── index-method-radio
    │   │   │       │   ├── assets
    │   │   │       │   │   ├── economy.svg
    │   │   │       │   │   └── high-quality.svg
    │   │   │       │   ├── index.module.css
    │   │   │       │   └── index.tsx
    │   │   │       └── permissions-radio
    │   │   │           ├── assets
    │   │   │           │   └── user.svg
    │   │   │           ├── index.module.css
    │   │   │           └── index.tsx
    │   │   ├── develop
    │   │   │   ├── code.tsx
    │   │   │   ├── doc.tsx
    │   │   │   ├── index.tsx
    │   │   │   ├── md.tsx
    │   │   │   ├── secret-key
    │   │   │   │   ├── assets
    │   │   │   │   │   ├── copied.svg
    │   │   │   │   │   ├── copy-hover.svg
    │   │   │   │   │   ├── copy.svg
    │   │   │   │   │   ├── pause.svg
    │   │   │   │   │   ├── play.svg
    │   │   │   │   │   ├── qrcode-hover.svg
    │   │   │   │   │   ├── qrcode.svg
    │   │   │   │   │   ├── svg.svg
    │   │   │   │   │   ├── svged.svg
    │   │   │   │   │   ├── trash-gray.svg
    │   │   │   │   │   └── trash-red.svg
    │   │   │   │   ├── input-copy.tsx
    │   │   │   │   ├── secret-key-button.tsx
    │   │   │   │   ├── secret-key-generate.tsx
    │   │   │   │   ├── secret-key-modal.tsx
    │   │   │   │   └── style.module.css
    │   │   │   ├── tag.tsx
    │   │   │   └── template
    │   │   │       ├── template.en.mdx
    │   │   │       ├── template.zh.mdx
    │   │   │       ├── template_advanced_chat.en.mdx
    │   │   │       ├── template_advanced_chat.zh.mdx
    │   │   │       ├── template_chat.en.mdx
    │   │   │       ├── template_chat.zh.mdx
    │   │   │       ├── template_workflow.en.mdx
    │   │   │       └── template_workflow.zh.mdx
    │   │   ├── explore
    │   │   │   ├── app-card
    │   │   │   │   └── index.tsx
    │   │   │   ├── app-list
    │   │   │   │   ├── index.tsx
    │   │   │   │   └── style.module.css
    │   │   │   ├── category.tsx
    │   │   │   ├── create-app-modal
    │   │   │   │   └── index.tsx
    │   │   │   ├── index.tsx
    │   │   │   ├── installed-app
    │   │   │   │   └── index.tsx
    │   │   │   ├── item-operation
    │   │   │   │   ├── index.tsx
    │   │   │   │   └── style.module.css
    │   │   │   └── sidebar
    │   │   │       ├── app-nav-item
    │   │   │       │   ├── index.tsx
    │   │   │       │   └── style.module.css
    │   │   │       └── index.tsx
    │   │   ├── header
    │   │   │   ├── HeaderWrapper.tsx
    │   │   │   ├── account-about
    │   │   │   │   ├── index.module.css
    │   │   │   │   └── index.tsx
    │   │   │   ├── account-dropdown
    │   │   │   │   ├── index.tsx
    │   │   │   │   └── workplace-selector
    │   │   │   │       ├── index.module.css
    │   │   │   │       └── index.tsx
    │   │   │   ├── account-setting
    │   │   │   │   ├── Integrations-page
    │   │   │   │   │   ├── index.module.css
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── account-page
    │   │   │   │   │   ├── index.module.css
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── api-based-extension-page
    │   │   │   │   │   ├── empty.tsx
    │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   ├── item.tsx
    │   │   │   │   │   ├── modal.tsx
    │   │   │   │   │   └── selector.tsx
    │   │   │   │   ├── collapse
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── data-source-page
    │   │   │   │   │   ├── data-source-notion
    │   │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   │   ├── operate
    │   │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   │   └── style.module.css
    │   │   │   │   │   ├── index.module.css
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── index.module.css
    │   │   │   │   ├── index.tsx
    │   │   │   │   ├── key-validator
    │   │   │   │   │   ├── KeyInput.tsx
    │   │   │   │   │   ├── Operate.tsx
    │   │   │   │   │   ├── ValidateStatus.tsx
    │   │   │   │   │   ├── declarations.ts
    │   │   │   │   │   ├── hooks.ts
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── language-page
    │   │   │   │   │   ├── index.module.css
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── members-page
    │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   ├── invite-modal
    │   │   │   │   │   │   ├── index.module.css
    │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   ├── invited-modal
    │   │   │   │   │   │   ├── assets
    │   │   │   │   │   │   │   ├── copied.svg
    │   │   │   │   │   │   │   ├── copy-hover.svg
    │   │   │   │   │   │   │   └── copy.svg
    │   │   │   │   │   │   ├── index.module.css
    │   │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   │   └── invitation-link.tsx
    │   │   │   │   │   └── operation
    │   │   │   │   │       ├── index.module.css
    │   │   │   │   │       └── index.tsx
    │   │   │   │   ├── model-provider-page
    │   │   │   │   │   ├── declarations.ts
    │   │   │   │   │   ├── hooks.ts
    │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   ├── model-badge
    │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   ├── model-icon
    │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   ├── model-modal
    │   │   │   │   │   │   ├── Form.tsx
    │   │   │   │   │   │   ├── Input.tsx
    │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   ├── model-name
    │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   ├── model-parameter-modal
    │   │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   │   ├── parameter-item.tsx
    │   │   │   │   │   │   ├── presets-parameter.tsx
    │   │   │   │   │   │   ├── stop-sequence.tsx
    │   │   │   │   │   │   └── trigger.tsx
    │   │   │   │   │   ├── model-selector
    │   │   │   │   │   │   ├── deprecated-model-trigger.tsx
    │   │   │   │   │   │   ├── empty-trigger.tsx
    │   │   │   │   │   │   ├── feature-icon.tsx
    │   │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   │   ├── model-trigger.tsx
    │   │   │   │   │   │   ├── popup-item.tsx
    │   │   │   │   │   │   ├── popup.tsx
    │   │   │   │   │   │   └── rerank-trigger.tsx
    │   │   │   │   │   ├── provider-added-card
    │   │   │   │   │   │   ├── add-model-button.tsx
    │   │   │   │   │   │   ├── credential-panel.tsx
    │   │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   │   ├── model-list.tsx
    │   │   │   │   │   │   ├── priority-selector.tsx
    │   │   │   │   │   │   ├── priority-use-tip.tsx
    │   │   │   │   │   │   ├── quota-panel.tsx
    │   │   │   │   │   │   └── tab.tsx
    │   │   │   │   │   ├── provider-card
    │   │   │   │   │   │   ├── index.module.css
    │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   ├── provider-icon
    │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   ├── system-model-selector
    │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   └── utils.ts
    │   │   │   │   └── plugin-page
    │   │   │   │       ├── SerpapiPlugin.tsx
    │   │   │   │       ├── index.tsx
    │   │   │   │       └── utils.ts
    │   │   │   ├── app-back
    │   │   │   │   └── index.tsx
    │   │   │   ├── app-nav
    │   │   │   │   └── index.tsx
    │   │   │   ├── app-selector
    │   │   │   │   └── index.tsx
    │   │   │   ├── assets
    │   │   │   │   ├── alpha.svg
    │   │   │   │   ├── anthropic.svg
    │   │   │   │   ├── azure.svg
    │   │   │   │   ├── bitbucket.svg
    │   │   │   │   ├── file.svg
    │   │   │   │   ├── github.svg
    │   │   │   │   ├── google.svg
    │   │   │   │   ├── gpt.svg
    │   │   │   │   ├── hugging-face.svg
    │   │   │   │   ├── notion.svg
    │   │   │   │   ├── salesforce.svg
    │   │   │   │   ├── serpapi.png
    │   │   │   │   ├── sync.svg
    │   │   │   │   ├── trash.svg
    │   │   │   │   └── twitter.svg
    │   │   │   ├── dataset-nav
    │   │   │   │   └── index.tsx
    │   │   │   ├── env-nav
    │   │   │   │   └── index.tsx
    │   │   │   ├── explore-nav
    │   │   │   │   └── index.tsx
    │   │   │   ├── github-star
    │   │   │   │   └── index.tsx
    │   │   │   ├── index.module.css
    │   │   │   ├── index.tsx
    │   │   │   ├── indicator
    │   │   │   │   └── index.tsx
    │   │   │   ├── maintenance-notice.tsx
    │   │   │   ├── nav
    │   │   │   │   ├── index.module.css
    │   │   │   │   ├── index.tsx
    │   │   │   │   └── nav-selector
    │   │   │   │       └── index.tsx
    │   │   │   └── tools-nav
    │   │   │       └── index.tsx
    │   │   ├── i18n-server.tsx
    │   │   ├── i18n.tsx
    │   │   ├── sentry-initor.tsx
    │   │   ├── share
    │   │   │   ├── chat
    │   │   │   │   ├── config-scence
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── hooks
    │   │   │   │   │   └── use-conversation.ts
    │   │   │   │   ├── index.tsx
    │   │   │   │   ├── sidebar
    │   │   │   │   │   ├── app-info
    │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   ├── card.module.css
    │   │   │   │   │   ├── card.tsx
    │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   ├── list
    │   │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   │   └── item.tsx
    │   │   │   │   │   └── rename-modal
    │   │   │   │   │       └── index.tsx
    │   │   │   │   ├── value-panel
    │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   └── style.module.css
    │   │   │   │   └── welcome
    │   │   │   │       ├── index.tsx
    │   │   │   │       ├── massive-component.tsx
    │   │   │   │       └── style.module.css
    │   │   │   ├── chatbot
    │   │   │   │   ├── config-scence
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── hooks
    │   │   │   │   │   └── use-conversation.ts
    │   │   │   │   ├── index.tsx
    │   │   │   │   ├── sidebar
    │   │   │   │   │   ├── app-info
    │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   ├── card.module.css
    │   │   │   │   │   ├── card.tsx
    │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   └── list
    │   │   │   │   │       ├── index.tsx
    │   │   │   │   │       └── style.module.css
    │   │   │   │   ├── value-panel
    │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   └── style.module.css
    │   │   │   │   └── welcome
    │   │   │   │       ├── index.tsx
    │   │   │   │       ├── massive-component.tsx
    │   │   │   │       └── style.module.css
    │   │   │   ├── header.tsx
    │   │   │   ├── text-generation
    │   │   │   │   ├── icons
    │   │   │   │   │   └── star.svg
    │   │   │   │   ├── index.tsx
    │   │   │   │   ├── no-data
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── result
    │   │   │   │   │   ├── content.tsx
    │   │   │   │   │   ├── header.tsx
    │   │   │   │   │   └── index.tsx
    │   │   │   │   ├── run-batch
    │   │   │   │   │   ├── csv-download
    │   │   │   │   │   │   └── index.tsx
    │   │   │   │   │   ├── csv-reader
    │   │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   │   └── style.module.css
    │   │   │   │   │   ├── index.tsx
    │   │   │   │   │   └── res-download
    │   │   │   │   │       └── index.tsx
    │   │   │   │   ├── run-once
    │   │   │   │   │   └── index.tsx
    │   │   │   │   └── style.module.css
    │   │   │   └── utils.ts
    │   │   ├── swr-initor.tsx
    │   │   ├── tools
    │   │   │   ├── contribute.tsx
    │   │   │   ├── edit-custom-collection-modal
    │   │   │   │   ├── config-credentials.tsx
    │   │   │   │   ├── examples.ts
    │   │   │   │   ├── get-schema.tsx
    │   │   │   │   ├── index.tsx
    │   │   │   │   └── test-api.tsx
    │   │   │   ├── index.tsx
    │   │   │   ├── info
    │   │   │   │   ├── no-custom-tool.tsx
    │   │   │   │   └── no-search-res.tsx
    │   │   │   ├── no-custom-tool-placeholder.tsx
    │   │   │   ├── search.tsx
    │   │   │   ├── setting
    │   │   │   │   └── build-in
    │   │   │   │       └── config-credentials.tsx
    │   │   │   ├── tool-list
    │   │   │   │   ├── header.tsx
    │   │   │   │   ├── index.tsx
    │   │   │   │   └── item.tsx
    │   │   │   ├── tool-nav-list
    │   │   │   │   ├── index.tsx
    │   │   │   │   └── item.tsx
    │   │   │   ├── types.ts
    │   │   │   └── utils
    │   │   │       ├── index.ts
    │   │   │       └── to-form-schema.ts
    │   │   ├── with-i18n.tsx
    │   │   └── workflow
    │   │       ├── block-icon.tsx
    │   │       ├── block-selector
    │   │       │   ├── blocks.tsx
    │   │       │   ├── constants.tsx
    │   │       │   ├── hooks.ts
    │   │       │   ├── index.tsx
    │   │       │   ├── tabs.tsx
    │   │       │   ├── tools.tsx
    │   │       │   └── types.ts
    │   │       ├── candidate-node.tsx
    │   │       ├── constants.ts
    │   │       ├── context.tsx
    │   │       ├── custom-connection-line.tsx
    │   │       ├── custom-edge.tsx
    │   │       ├── features.tsx
    │   │       ├── header
    │   │       │   ├── checklist.tsx
    │   │       │   ├── editing-title.tsx
    │   │       │   ├── index.tsx
    │   │       │   ├── restoring-title.tsx
    │   │       │   ├── run-and-history.tsx
    │   │       │   ├── running-title.tsx
    │   │       │   └── view-history.tsx
    │   │       ├── help-line
    │   │       │   ├── index.tsx
    │   │       │   └── types.ts
    │   │       ├── hooks
    │   │       │   ├── index.ts
    │   │       │   ├── use-checklist.ts
    │   │       │   ├── use-edges-interactions.ts
    │   │       │   ├── use-node-data-update.ts
    │   │       │   ├── use-nodes-data.ts
    │   │       │   ├── use-nodes-interactions.ts
    │   │       │   ├── use-nodes-sync-draft.ts
    │   │       │   ├── use-panel-interactions.ts
    │   │       │   ├── use-selection-interactions.ts
    │   │       │   ├── use-workflow-interactions.ts
    │   │       │   ├── use-workflow-mode.ts
    │   │       │   ├── use-workflow-run.ts
    │   │       │   ├── use-workflow-start-run.tsx
    │   │       │   ├── use-workflow-template.ts
    │   │       │   └── use-workflow.ts
    │   │       ├── index.tsx
    │   │       ├── node-contextmenu.tsx
    │   │       ├── nodes
    │   │       │   ├── _base
    │   │       │   │   ├── components
    │   │       │   │   │   ├── add-button.tsx
    │   │       │   │   │   ├── before-run-form
    │   │       │   │   │   │   ├── form-item.tsx
    │   │       │   │   │   │   ├── form.tsx
    │   │       │   │   │   │   └── index.tsx
    │   │       │   │   │   ├── editor
    │   │       │   │   │   │   ├── base.tsx
    │   │       │   │   │   │   ├── code-editor
    │   │       │   │   │   │   │   ├── editor-support-vars.tsx
    │   │       │   │   │   │   │   ├── index.tsx
    │   │       │   │   │   │   │   └── style.css
    │   │       │   │   │   │   ├── text-editor.tsx
    │   │       │   │   │   │   └── wrap.tsx
    │   │       │   │   │   ├── field.tsx
    │   │       │   │   │   ├── info-panel.tsx
    │   │       │   │   │   ├── input-support-select-var.tsx
    │   │       │   │   │   ├── input-var-type-icon.tsx
    │   │       │   │   │   ├── memory-config.tsx
    │   │       │   │   │   ├── next-step
    │   │       │   │   │   │   ├── add.tsx
    │   │       │   │   │   │   ├── index.tsx
    │   │       │   │   │   │   ├── item.tsx
    │   │       │   │   │   │   └── line.tsx
    │   │       │   │   │   ├── node-control.tsx
    │   │       │   │   │   ├── node-handle.tsx
    │   │       │   │   │   ├── output-vars.tsx
    │   │       │   │   │   ├── panel-operator
    │   │       │   │   │   │   ├── change-block.tsx
    │   │       │   │   │   │   ├── index.tsx
    │   │       │   │   │   │   └── panel-operator-popup.tsx
    │   │       │   │   │   ├── prompt
    │   │       │   │   │   │   └── editor.tsx
    │   │       │   │   │   ├── readonly-input-with-select-var.tsx
    │   │       │   │   │   ├── remove-button.tsx
    │   │       │   │   │   ├── remove-effect-var-confirm.tsx
    │   │       │   │   │   ├── selector.tsx
    │   │       │   │   │   ├── split.tsx
    │   │       │   │   │   ├── support-var-input
    │   │       │   │   │   │   └── index.tsx
    │   │       │   │   │   ├── title-description-input.tsx
    │   │       │   │   │   ├── toggle-expand-btn.tsx
    │   │       │   │   │   └── variable
    │   │       │   │   │       ├── output-var-list.tsx
    │   │       │   │   │       ├── utils.ts
    │   │       │   │   │       ├── var-list.tsx
    │   │       │   │   │       ├── var-reference-picker.tsx
    │   │       │   │   │       ├── var-reference-popup.tsx
    │   │       │   │   │       ├── var-reference-vars.tsx
    │   │       │   │   │       └── var-type-picker.tsx
    │   │       │   │   ├── hooks
    │   │       │   │   │   ├── use-available-var-list.ts
    │   │       │   │   │   ├── use-node-crud.ts
    │   │       │   │   │   ├── use-one-step-run.ts
    │   │       │   │   │   ├── use-output-var-list.ts
    │   │       │   │   │   ├── use-resize-panel.ts
    │   │       │   │   │   ├── use-toggle-expend.ts
    │   │       │   │   │   └── use-var-list.ts
    │   │       │   │   ├── node.tsx
    │   │       │   │   └── panel.tsx
    │   │       │   ├── answer
    │   │       │   │   ├── default.ts
    │   │       │   │   ├── node.tsx
    │   │       │   │   ├── panel.tsx
    │   │       │   │   ├── types.ts
    │   │       │   │   ├── use-config.ts
    │   │       │   │   └── utils.ts
    │   │       │   ├── code
    │   │       │   │   ├── default.ts
    │   │       │   │   ├── dependency-picker.tsx
    │   │       │   │   ├── dependency.tsx
    │   │       │   │   ├── node.tsx
    │   │       │   │   ├── panel.tsx
    │   │       │   │   ├── types.ts
    │   │       │   │   ├── use-config.ts
    │   │       │   │   └── utils.ts
    │   │       │   ├── constants.ts
    │   │       │   ├── end
    │   │       │   │   ├── default.ts
    │   │       │   │   ├── node.tsx
    │   │       │   │   ├── panel.tsx
    │   │       │   │   ├── types.ts
    │   │       │   │   ├── use-config.ts
    │   │       │   │   └── utils.ts
    │   │       │   ├── http
    │   │       │   │   ├── components
    │   │       │   │   │   ├── api-input.tsx
    │   │       │   │   │   ├── authorization
    │   │       │   │   │   │   ├── index.tsx
    │   │       │   │   │   │   └── radio-group.tsx
    │   │       │   │   │   ├── edit-body
    │   │       │   │   │   │   └── index.tsx
    │   │       │   │   │   ├── key-value
    │   │       │   │   │   │   ├── bulk-edit
    │   │       │   │   │   │   │   └── index.tsx
    │   │       │   │   │   │   ├── index.tsx
    │   │       │   │   │   │   └── key-value-edit
    │   │       │   │   │   │       ├── index.tsx
    │   │       │   │   │   │       ├── input-item.tsx
    │   │       │   │   │   │       └── item.tsx
    │   │       │   │   │   └── timeout
    │   │       │   │   │       └── index.tsx
    │   │       │   │   ├── default.ts
    │   │       │   │   ├── hooks
    │   │       │   │   │   └── use-key-value-list.ts
    │   │       │   │   ├── node.tsx
    │   │       │   │   ├── panel.tsx
    │   │       │   │   ├── types.ts
    │   │       │   │   ├── use-config.ts
    │   │       │   │   └── utils.ts
    │   │       │   ├── if-else
    │   │       │   │   ├── components
    │   │       │   │   │   ├── condition-item.tsx
    │   │       │   │   │   └── condition-list.tsx
    │   │       │   │   ├── default.ts
    │   │       │   │   ├── node.tsx
    │   │       │   │   ├── panel.tsx
    │   │       │   │   ├── types.ts
    │   │       │   │   ├── use-config.ts
    │   │       │   │   └── utils.ts
    │   │       │   ├── index.tsx
    │   │       │   ├── knowledge-retrieval
    │   │       │   │   ├── components
    │   │       │   │   │   ├── add-dataset.tsx
    │   │       │   │   │   ├── dataset-item.tsx
    │   │       │   │   │   ├── dataset-list.tsx
    │   │       │   │   │   └── retrieval-config.tsx
    │   │       │   │   ├── default.ts
    │   │       │   │   ├── node.tsx
    │   │       │   │   ├── panel.tsx
    │   │       │   │   ├── types.ts
    │   │       │   │   ├── use-config.ts
    │   │       │   │   └── utils.ts
    │   │       │   ├── llm
    │   │       │   │   ├── components
    │   │       │   │   │   ├── config-prompt-item.tsx
    │   │       │   │   │   ├── config-prompt.tsx
    │   │       │   │   │   └── resolution-picker.tsx
    │   │       │   │   ├── default.ts
    │   │       │   │   ├── node.tsx
    │   │       │   │   ├── panel.tsx
    │   │       │   │   ├── types.ts
    │   │       │   │   ├── use-config.ts
    │   │       │   │   └── utils.ts
    │   │       │   ├── question-classifier
    │   │       │   │   ├── components
    │   │       │   │   │   ├── advanced-setting.tsx
    │   │       │   │   │   ├── class-item.tsx
    │   │       │   │   │   └── class-list.tsx
    │   │       │   │   ├── default.ts
    │   │       │   │   ├── node.tsx
    │   │       │   │   ├── panel.tsx
    │   │       │   │   ├── types.ts
    │   │       │   │   ├── use-config.ts
    │   │       │   │   └── utils.ts
    │   │       │   ├── start
    │   │       │   │   ├── components
    │   │       │   │   │   ├── var-item.tsx
    │   │       │   │   │   └── var-list.tsx
    │   │       │   │   ├── default.ts
    │   │       │   │   ├── node.tsx
    │   │       │   │   ├── panel.tsx
    │   │       │   │   ├── types.ts
    │   │       │   │   ├── use-config.ts
    │   │       │   │   └── utils.ts
    │   │       │   ├── template-transform
    │   │       │   │   ├── default.ts
    │   │       │   │   ├── node.tsx
    │   │       │   │   ├── panel.tsx
    │   │       │   │   ├── types.ts
    │   │       │   │   ├── use-config.ts
    │   │       │   │   └── utils.ts
    │   │       │   ├── tool
    │   │       │   │   ├── components
    │   │       │   │   │   └── input-var-list.tsx
    │   │       │   │   ├── default.ts
    │   │       │   │   ├── node.tsx
    │   │       │   │   ├── panel.tsx
    │   │       │   │   ├── types.ts
    │   │       │   │   ├── use-config.ts
    │   │       │   │   └── utils.ts
    │   │       │   └── variable-assigner
    │   │       │       ├── components
    │   │       │       │   └── var-list
    │   │       │       │       ├── index.tsx
    │   │       │       │       └── use-var-list.ts
    │   │       │       ├── default.ts
    │   │       │       ├── node.tsx
    │   │       │       ├── panel.tsx
    │   │       │       ├── types.ts
    │   │       │       ├── use-config.ts
    │   │       │       └── utils.ts
    │   │       ├── operator
    │   │       │   ├── add-block.tsx
    │   │       │   ├── control.tsx
    │   │       │   ├── index.tsx
    │   │       │   ├── tip-popup.tsx
    │   │       │   └── zoom-in-out.tsx
    │   │       ├── panel
    │   │       │   ├── chat-record
    │   │       │   │   ├── index.tsx
    │   │       │   │   └── user-input.tsx
    │   │       │   ├── debug-and-preview
    │   │       │   │   ├── chat-wrapper.tsx
    │   │       │   │   ├── empty.tsx
    │   │       │   │   ├── hooks.ts
    │   │       │   │   ├── index.tsx
    │   │       │   │   └── user-input.tsx
    │   │       │   ├── index.tsx
    │   │       │   ├── inputs-panel.tsx
    │   │       │   ├── record.tsx
    │   │       │   └── workflow-preview.tsx
    │   │       ├── panel-contextmenu.tsx
    │   │       ├── run
    │   │       │   ├── index.tsx
    │   │       │   ├── meta.tsx
    │   │       │   ├── node.tsx
    │   │       │   ├── output-panel.tsx
    │   │       │   ├── result-panel.tsx
    │   │       │   ├── result-text.tsx
    │   │       │   ├── status.tsx
    │   │       │   └── tracing-panel.tsx
    │   │       ├── shortcuts-name.tsx
    │   │       ├── store.ts
    │   │       ├── style.css
    │   │       ├── types.ts
    │   │       └── utils.ts
    │   ├── init
    │   │   ├── InitPasswordPopup.tsx
    │   │   └── page.tsx
    │   ├── install
    │   │   ├── installForm.tsx
    │   │   └── page.tsx
    │   ├── layout.tsx
    │   ├── page.module.css
    │   ├── page.tsx
    │   ├── signin
    │   │   ├── _header.tsx
    │   │   ├── assets
    │   │   │   ├── background.png
    │   │   │   ├── github.svg
    │   │   │   └── google.svg
    │   │   ├── forms.tsx
    │   │   ├── normalForm.tsx
    │   │   ├── oneMoreStep.tsx
    │   │   ├── page.module.css
    │   │   ├── page.tsx
    │   │   └── userSSOForm.tsx
    │   └── styles
    │       ├── globals.css
    │       └── markdown.scss
    ├── assets
    │   ├── action.svg
    │   ├── csv.svg
    │   ├── delete.svg
    │   ├── doc.svg
    │   ├── docx.svg
    │   ├── html.svg
    │   ├── json.svg
    │   ├── md.svg
    │   ├── pdf.svg
    │   ├── txt.svg
    │   └── xlsx.svg
    ├── bin
    │   └── uglify-embed.js
    ├── config
    │   └── index.ts
    ├── context
    │   ├── app-context.tsx
    │   ├── dataset-detail.ts
    │   ├── datasets-context.tsx
    │   ├── debug-configuration.ts
    │   ├── event-emitter.tsx
    │   ├── explore-context.ts
    │   ├── i18n.ts
    │   ├── modal-context.tsx
    │   ├── provider-context.tsx
    │   └── workspace-context.tsx
    ├── docker
    │   ├── entrypoint.sh
    │   └── pm2.json
    ├── folder-structure.md
    ├── global.d.ts
    ├── hooks
    │   ├── use-breakpoints.ts
    │   ├── use-metadata.ts
    │   ├── use-moderate.ts
    │   ├── use-pay.tsx
    │   ├── use-tab-searchparams.ts
    │   └── use-timestamp.ts
    ├── i18n
    │   ├── README.md
    │   ├── de-DE
    │   │   ├── app-annotation.ts
    │   │   ├── app-api.ts
    │   │   ├── app-debug.ts
    │   │   ├── app-log.ts
    │   │   ├── app-overview.ts
    │   │   ├── app.ts
    │   │   ├── billing.ts
    │   │   ├── common.ts
    │   │   ├── custom.ts
    │   │   ├── dataset-creation.ts
    │   │   ├── dataset-documents.ts
    │   │   ├── dataset-hit-testing.ts
    │   │   ├── dataset-settings.ts
    │   │   ├── dataset.ts
    │   │   ├── explore.ts
    │   │   ├── layout.ts
    │   │   ├── login.ts
    │   │   ├── register.ts
    │   │   ├── run-log.ts
    │   │   ├── share-app.ts
    │   │   ├── tools.ts
    │   │   └── workflow.ts
    │   ├── en-US
    │   │   ├── app-annotation.ts
    │   │   ├── app-api.ts
    │   │   ├── app-debug.ts
    │   │   ├── app-log.ts
    │   │   ├── app-overview.ts
    │   │   ├── app.ts
    │   │   ├── billing.ts
    │   │   ├── common.ts
    │   │   ├── custom.ts
    │   │   ├── dataset-creation.ts
    │   │   ├── dataset-documents.ts
    │   │   ├── dataset-hit-testing.ts
    │   │   ├── dataset-settings.ts
    │   │   ├── dataset.ts
    │   │   ├── explore.ts
    │   │   ├── layout.ts
    │   │   ├── login.ts
    │   │   ├── register.ts
    │   │   ├── run-log.ts
    │   │   ├── share-app.ts
    │   │   ├── tools.ts
    │   │   └── workflow.ts
    │   ├── fr-FR
    │   │   ├── app-annotation.ts
    │   │   ├── app-api.ts
    │   │   ├── app-debug.ts
    │   │   ├── app-log.ts
    │   │   ├── app-overview.ts
    │   │   ├── app.ts
    │   │   ├── billing.ts
    │   │   ├── common.ts
    │   │   ├── custom.ts
    │   │   ├── dataset-creation.ts
    │   │   ├── dataset-documents.ts
    │   │   ├── dataset-hit-testing.ts
    │   │   ├── dataset-settings.ts
    │   │   ├── dataset.ts
    │   │   ├── explore.ts
    │   │   ├── layout.ts
    │   │   ├── login.ts
    │   │   ├── register.ts
    │   │   ├── run-log.ts
    │   │   ├── share-app.ts
    │   │   ├── tools.ts
    │   │   └── workflow.ts
    │   ├── i18next-config.ts
    │   ├── index.ts
    │   ├── ja-JP
    │   │   ├── app-annotation.ts
    │   │   ├── app-api.ts
    │   │   ├── app-debug.ts
    │   │   ├── app-log.ts
    │   │   ├── app-overview.ts
    │   │   ├── app.ts
    │   │   ├── billing.ts
    │   │   ├── common.ts
    │   │   ├── custom.ts
    │   │   ├── dataset-creation.ts
    │   │   ├── dataset-documents.ts
    │   │   ├── dataset-hit-testing.ts
    │   │   ├── dataset-settings.ts
    │   │   ├── dataset.ts
    │   │   ├── explore.ts
    │   │   ├── layout.ts
    │   │   ├── login.ts
    │   │   ├── register.ts
    │   │   ├── run-log.ts
    │   │   ├── share-app.ts
    │   │   ├── tools.ts
    │   │   └── workflow.ts
    │   ├── ko-KR
    │   │   ├── app-annotation.ts
    │   │   ├── app-api.ts
    │   │   ├── app-debug.ts
    │   │   ├── app-log.ts
    │   │   ├── app-overview.ts
    │   │   ├── app.ts
    │   │   ├── billing.ts
    │   │   ├── common.ts
    │   │   ├── custom.ts
    │   │   ├── dataset-creation.ts
    │   │   ├── dataset-documents.ts
    │   │   ├── dataset-hit-testing.ts
    │   │   ├── dataset-settings.ts
    │   │   ├── dataset.ts
    │   │   ├── explore.ts
    │   │   ├── layout.ts
    │   │   ├── login.ts
    │   │   ├── register.ts
    │   │   ├── run-log.ts
    │   │   ├── share-app.ts
    │   │   ├── tools.ts
    │   │   └── workflow.ts
    │   ├── language.ts
    │   ├── pl-PL
    │   │   ├── app-annotation.ts
    │   │   ├── app-api.ts
    │   │   ├── app-debug.ts
    │   │   ├── app-log.ts
    │   │   ├── app-overview.ts
    │   │   ├── app.ts
    │   │   ├── billing.ts
    │   │   ├── common.ts
    │   │   ├── custom.ts
    │   │   ├── dataset-creation.ts
    │   │   ├── dataset-documents.ts
    │   │   ├── dataset-hit-testing.ts
    │   │   ├── dataset-settings.ts
    │   │   ├── dataset.ts
    │   │   ├── explore.ts
    │   │   ├── layout.ts
    │   │   ├── login.ts
    │   │   ├── register.ts
    │   │   ├── run-log.ts
    │   │   ├── share-app.ts
    │   │   ├── tools.ts
    │   │   └── workflow.ts
    │   ├── pt-BR
    │   │   ├── app-annotation.ts
    │   │   ├── app-api.ts
    │   │   ├── app-debug.ts
    │   │   ├── app-log.ts
    │   │   ├── app-overview.ts
    │   │   ├── app.ts
    │   │   ├── billing.ts
    │   │   ├── common.ts
    │   │   ├── custom.ts
    │   │   ├── dataset-creation.ts
    │   │   ├── dataset-documents.ts
    │   │   ├── dataset-hit-testing.ts
    │   │   ├── dataset-settings.ts
    │   │   ├── dataset.ts
    │   │   ├── explore.ts
    │   │   ├── layout.ts
    │   │   ├── login.ts
    │   │   ├── register.ts
    │   │   ├── run-log.ts
    │   │   ├── share-app.ts
    │   │   ├── tools.ts
    │   │   └── workflow.ts
    │   ├── ro-RO
    │   │   ├── app-annotation.ts
    │   │   ├── app-api.ts
    │   │   ├── app-debug.ts
    │   │   ├── app-log.ts
    │   │   ├── app-overview.ts
    │   │   ├── app.ts
    │   │   ├── billing.ts
    │   │   ├── common.ts
    │   │   ├── custom.ts
    │   │   ├── dataset-creation.ts
    │   │   ├── dataset-documents.ts
    │   │   ├── dataset-hit-testing.ts
    │   │   ├── dataset-settings.ts
    │   │   ├── dataset.ts
    │   │   ├── explore.ts
    │   │   ├── layout.ts
    │   │   ├── login.ts
    │   │   ├── register.ts
    │   │   ├── run-log.ts
    │   │   ├── share-app.ts
    │   │   ├── tools.ts
    │   │   └── workflow.ts
    │   ├── script.js
    │   ├── server.ts
    │   ├── uk-UA
    │   │   ├── app-annotation.ts
    │   │   ├── app-api.ts
    │   │   ├── app-debug.ts
    │   │   ├── app-log.ts
    │   │   ├── app-overview.ts
    │   │   ├── app.ts
    │   │   ├── billing.ts
    │   │   ├── common.ts
    │   │   ├── custom.ts
    │   │   ├── dataset-creation.ts
    │   │   ├── dataset-documents.ts
    │   │   ├── dataset-hit-testing.ts
    │   │   ├── dataset-settings.ts
    │   │   ├── dataset.ts
    │   │   ├── explore.ts
    │   │   ├── layout.ts
    │   │   ├── login.ts
    │   │   ├── register.ts
    │   │   ├── run-log.ts
    │   │   ├── share-app.ts
    │   │   ├── tools.ts
    │   │   └── workflow.ts
    │   ├── vi-VN
    │   │   ├── app-annotation.ts
    │   │   ├── app-api.ts
    │   │   ├── app-debug.ts
    │   │   ├── app-log.ts
    │   │   ├── app-overview.ts
    │   │   ├── app.ts
    │   │   ├── billing.ts
    │   │   ├── common.ts
    │   │   ├── custom.ts
    │   │   ├── dataset-creation.ts
    │   │   ├── dataset-documents.ts
    │   │   ├── dataset-hit-testing.ts
    │   │   ├── dataset-settings.ts
    │   │   ├── dataset.ts
    │   │   ├── explore.ts
    │   │   ├── layout.ts
    │   │   ├── login.ts
    │   │   ├── register.ts
    │   │   ├── run-log.ts
    │   │   ├── share-app.ts
    │   │   ├── tools.ts
    │   │   └── workflow.ts
    │   ├── zh-Hans
    │   │   ├── app-annotation.ts
    │   │   ├── app-api.ts
    │   │   ├── app-debug.ts
    │   │   ├── app-log.ts
    │   │   ├── app-overview.ts
    │   │   ├── app.ts
    │   │   ├── billing.ts
    │   │   ├── common.ts
    │   │   ├── custom.ts
    │   │   ├── dataset-creation.ts
    │   │   ├── dataset-documents.ts
    │   │   ├── dataset-hit-testing.ts
    │   │   ├── dataset-settings.ts
    │   │   ├── dataset.ts
    │   │   ├── explore.ts
    │   │   ├── layout.ts
    │   │   ├── login.ts
    │   │   ├── register.ts
    │   │   ├── run-log.ts
    │   │   ├── share-app.ts
    │   │   ├── tools.ts
    │   │   └── workflow.ts
    │   └── zh-Hant
    │       ├── app-annotation.ts
    │       ├── app-api.ts
    │       ├── app-debug.ts
    │       ├── app-log.ts
    │       ├── app-overview.ts
    │       ├── app.ts
    │       ├── billing.ts
    │       ├── common.ts
    │       ├── custom.ts
    │       ├── dataset-creation.ts
    │       ├── dataset-documents.ts
    │       ├── dataset-hit-testing.ts
    │       ├── dataset-settings.ts
    │       ├── dataset.ts
    │       ├── explore.ts
    │       ├── layout.ts
    │       ├── login.ts
    │       ├── register.ts
    │       ├── run-log.ts
    │       ├── share-app.ts
    │       ├── tools.ts
    │       └── workflow.ts
    ├── models
    │   ├── app.ts
    │   ├── common.ts
    │   ├── datasets.ts
    │   ├── debug.ts
    │   ├── explore.ts
    │   ├── log.ts
    │   ├── share.ts
    │   └── user.ts
    ├── next.config.js
    ├── package.json
    ├── postcss.config.js
    ├── public
    │   ├── embed.js
    │   ├── embed.min.js
    │   ├── favicon.ico
    │   ├── logo
    │   │   ├── logo-embeded-chat-avatar.png
    │   │   ├── logo-embeded-chat-header.png
    │   │   └── logo-site.png
    │   └── vs
    │       ├── base
    │       │   ├── browser
    │       │   │   └── ui
    │       │   │       └── codicons
    │       │   │           └── codicon
    │       │   │               └── codicon.ttf
    │       │   ├── common
    │       │   │   └── worker
    │       │   │       ├── simpleWorker.nls.de.js
    │       │   │       ├── simpleWorker.nls.es.js
    │       │   │       ├── simpleWorker.nls.fr.js
    │       │   │       ├── simpleWorker.nls.it.js
    │       │   │       ├── simpleWorker.nls.ja.js
    │       │   │       ├── simpleWorker.nls.js
    │       │   │       ├── simpleWorker.nls.ko.js
    │       │   │       ├── simpleWorker.nls.ru.js
    │       │   │       ├── simpleWorker.nls.zh-cn.js
    │       │   │       └── simpleWorker.nls.zh-tw.js
    │       │   └── worker
    │       │       └── workerMain.js
    │       ├── basic-languages
    │       │   ├── abap
    │       │   │   └── abap.js
    │       │   ├── apex
    │       │   │   └── apex.js
    │       │   ├── azcli
    │       │   │   └── azcli.js
    │       │   ├── bat
    │       │   │   └── bat.js
    │       │   ├── bicep
    │       │   │   └── bicep.js
    │       │   ├── cameligo
    │       │   │   └── cameligo.js
    │       │   ├── clojure
    │       │   │   └── clojure.js
    │       │   ├── coffee
    │       │   │   └── coffee.js
    │       │   ├── cpp
    │       │   │   └── cpp.js
    │       │   ├── csharp
    │       │   │   └── csharp.js
    │       │   ├── csp
    │       │   │   └── csp.js
    │       │   ├── css
    │       │   │   └── css.js
    │       │   ├── cypher
    │       │   │   └── cypher.js
    │       │   ├── dart
    │       │   │   └── dart.js
    │       │   ├── dockerfile
    │       │   │   └── dockerfile.js
    │       │   ├── ecl
    │       │   │   └── ecl.js
    │       │   ├── elixir
    │       │   │   └── elixir.js
    │       │   ├── flow9
    │       │   │   └── flow9.js
    │       │   ├── freemarker2
    │       │   │   └── freemarker2.js
    │       │   ├── fsharp
    │       │   │   └── fsharp.js
    │       │   ├── go
    │       │   │   └── go.js
    │       │   ├── graphql
    │       │   │   └── graphql.js
    │       │   ├── handlebars
    │       │   │   └── handlebars.js
    │       │   ├── hcl
    │       │   │   └── hcl.js
    │       │   ├── html
    │       │   │   └── html.js
    │       │   ├── ini
    │       │   │   └── ini.js
    │       │   ├── java
    │       │   │   └── java.js
    │       │   ├── javascript
    │       │   │   └── javascript.js
    │       │   ├── julia
    │       │   │   └── julia.js
    │       │   ├── kotlin
    │       │   │   └── kotlin.js
    │       │   ├── less
    │       │   │   └── less.js
    │       │   ├── lexon
    │       │   │   └── lexon.js
    │       │   ├── liquid
    │       │   │   └── liquid.js
    │       │   ├── lua
    │       │   │   └── lua.js
    │       │   ├── m3
    │       │   │   └── m3.js
    │       │   ├── markdown
    │       │   │   └── markdown.js
    │       │   ├── mdx
    │       │   │   └── mdx.js
    │       │   ├── mips
    │       │   │   └── mips.js
    │       │   ├── msdax
    │       │   │   └── msdax.js
    │       │   ├── mysql
    │       │   │   └── mysql.js
    │       │   ├── objective-c
    │       │   │   └── objective-c.js
    │       │   ├── pascal
    │       │   │   └── pascal.js
    │       │   ├── pascaligo
    │       │   │   └── pascaligo.js
    │       │   ├── perl
    │       │   │   └── perl.js
    │       │   ├── pgsql
    │       │   │   └── pgsql.js
    │       │   ├── php
    │       │   │   └── php.js
    │       │   ├── pla
    │       │   │   └── pla.js
    │       │   ├── postiats
    │       │   │   └── postiats.js
    │       │   ├── powerquery
    │       │   │   └── powerquery.js
    │       │   ├── powershell
    │       │   │   └── powershell.js
    │       │   ├── protobuf
    │       │   │   └── protobuf.js
    │       │   ├── pug
    │       │   │   └── pug.js
    │       │   ├── python
    │       │   │   └── python.js
    │       │   ├── qsharp
    │       │   │   └── qsharp.js
    │       │   ├── r
    │       │   │   └── r.js
    │       │   ├── razor
    │       │   │   └── razor.js
    │       │   ├── redis
    │       │   │   └── redis.js
    │       │   ├── redshift
    │       │   │   └── redshift.js
    │       │   ├── restructuredtext
    │       │   │   └── restructuredtext.js
    │       │   ├── ruby
    │       │   │   └── ruby.js
    │       │   ├── rust
    │       │   │   └── rust.js
    │       │   ├── sb
    │       │   │   └── sb.js
    │       │   ├── scala
    │       │   │   └── scala.js
    │       │   ├── scheme
    │       │   │   └── scheme.js
    │       │   ├── scss
    │       │   │   └── scss.js
    │       │   ├── shell
    │       │   │   └── shell.js
    │       │   ├── solidity
    │       │   │   └── solidity.js
    │       │   ├── sophia
    │       │   │   └── sophia.js
    │       │   ├── sparql
    │       │   │   └── sparql.js
    │       │   ├── sql
    │       │   │   └── sql.js
    │       │   ├── st
    │       │   │   └── st.js
    │       │   ├── swift
    │       │   │   └── swift.js
    │       │   ├── systemverilog
    │       │   │   └── systemverilog.js
    │       │   ├── tcl
    │       │   │   └── tcl.js
    │       │   ├── twig
    │       │   │   └── twig.js
    │       │   ├── typescript
    │       │   │   └── typescript.js
    │       │   ├── vb
    │       │   │   └── vb.js
    │       │   ├── wgsl
    │       │   │   └── wgsl.js
    │       │   ├── xml
    │       │   │   └── xml.js
    │       │   └── yaml
    │       │       └── yaml.js
    │       ├── editor
    │       │   ├── editor.main.css
    │       │   ├── editor.main.js
    │       │   ├── editor.main.nls.de.js
    │       │   ├── editor.main.nls.es.js
    │       │   ├── editor.main.nls.fr.js
    │       │   ├── editor.main.nls.it.js
    │       │   ├── editor.main.nls.ja.js
    │       │   ├── editor.main.nls.js
    │       │   ├── editor.main.nls.ko.js
    │       │   ├── editor.main.nls.ru.js
    │       │   ├── editor.main.nls.zh-cn.js
    │       │   └── editor.main.nls.zh-tw.js
    │       ├── language
    │       │   ├── css
    │       │   │   ├── cssMode.js
    │       │   │   └── cssWorker.js
    │       │   ├── html
    │       │   │   ├── htmlMode.js
    │       │   │   └── htmlWorker.js
    │       │   ├── json
    │       │   │   ├── jsonMode.js
    │       │   │   └── jsonWorker.js
    │       │   └── typescript
    │       │       ├── tsMode.js
    │       │       └── tsWorker.js
    │       └── loader.js
    ├── service
    │   ├── annotation.ts
    │   ├── apps.ts
    │   ├── base.ts
    │   ├── billing.ts
    │   ├── common.ts
    │   ├── datasets.ts
    │   ├── debug.ts
    │   ├── demo
    │   │   └── index.tsx
    │   ├── explore.ts
    │   ├── log.ts
    │   ├── share.ts
    │   ├── sso.ts
    │   ├── tag.ts
    │   ├── tools.ts
    │   └── workflow.ts
    ├── tailwind.config.js
    ├── tsconfig.json
    ├── types
    │   ├── app.ts
    │   ├── feature.ts
    │   └── workflow.ts
    ├── typography.js
    ├── utils
    │   ├── app-redirection.ts
    │   ├── format.ts
    │   ├── index.ts
    │   ├── model-config.ts
    │   ├── timezone.json
    │   ├── timezone.ts
    │   └── var.ts
    └── yarn.lock

```
