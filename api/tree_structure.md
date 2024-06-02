## api file and folder tree structure

   │   │   │   └── xinference_helper.py
│   │   │   ├── yi
│   │   │   │   ├── __init__.py
│   │   │   │   ├── _assets
│   │   │   │   │   ├── icon_l_en.svg
│   │   │   │   │   └── icon_s_en.svg
│   │   │   │   ├── llm
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── _position.yaml
│   │   │   │   │   ├── llm.py
│   │   │   │   │   ├── yi-34b-chat-0205.yaml
│   │   │   │   │   ├── yi-34b-chat-200k.yaml
│   │   │   │   │   ├── yi-large-turbo.yaml
│   │   │   │   │   ├── yi-large.yaml
│   │   │   │   │   ├── yi-medium-200k.yaml
│   │   │   │   │   ├── yi-medium.yaml
│   │   │   │   │   ├── yi-spark.yaml
│   │   │   │   │   ├── yi-vision.yaml
│   │   │   │   │   └── yi-vl-plus.yaml
│   │   │   │   ├── yi.py
│   │   │   │   └── yi.yaml
│   │   │   └── zhipuai
│   │   │       ├── __init__.py
│   │   │       ├── _assets
│   │   │       │   ├── icon_l_en.svg
│   │   │       │   ├── icon_l_zh.svg
│   │   │       │   └── icon_s_en.svg
│   │   │       ├── _common.py
│   │   │       ├── llm
│   │   │       │   ├── __init__.py
│   │   │       │   ├── chatglm_lite.yaml
│   │   │       │   ├── chatglm_lite_32k.yaml
│   │   │       │   ├── chatglm_pro.yaml
│   │   │       │   ├── chatglm_std.yaml
│   │   │       │   ├── chatglm_turbo.yaml
│   │   │       │   ├── glm_3_turbo.yaml
│   │   │       │   ├── glm_4.yaml
│   │   │       │   ├── glm_4v.yaml
│   │   │       │   └── llm.py
│   │   │       ├── text_embedding
│   │   │       │   ├── __init__.py
│   │   │       │   ├── text_embedding.py
│   │   │       │   └── text_embedding.yaml
│   │   │       ├── zhipuai.py
│   │   │       ├── zhipuai.yaml
│   │   │       └── zhipuai_sdk
│   │   │           ├── __init__.py
│   │   │           ├── __version__.py
│   │   │           ├── _client.py
│   │   │           ├── api_resource
│   │   │           ├── core
│   │   │           └── types
│   │   ├── schema_validators
│   │   │   ├── __init__.py
│   │   │   ├── common_validator.py
│   │   │   ├── model_credential_schema_validator.py
│   │   │   └── provider_credential_schema_validator.py
│   │   └── utils
│   │       ├── __init__.py
│   │       ├── _compat.py
│   │       ├── encoders.py
│   │       └── helper.py
│   ├── moderation
│   │   ├── __init__.py
│   │   ├── api
│   │   │   ├── __builtin__
│   │   │   ├── __init__.py
│   │   │   └── api.py
│   │   ├── base.py
│   │   ├── factory.py
│   │   ├── input_moderation.py
│   │   ├── keywords
│   │   │   ├── __builtin__
│   │   │   ├── __init__.py
│   │   │   └── keywords.py
│   │   ├── openai_moderation
│   │   │   ├── __builtin__
│   │   │   ├── __init__.py
│   │   │   └── openai_moderation.py
│   │   └── output_moderation.py
│   ├── prompt
│   │   ├── __init__.py
│   │   ├── advanced_prompt_transform.py
│   │   ├── entities
│   │   │   ├── __init__.py
│   │   │   └── advanced_prompt_entities.py
│   │   ├── prompt_templates
│   │   │   ├── __init__.py
│   │   │   ├── advanced_prompt_templates.py
│   │   │   ├── baichuan_chat.json
│   │   │   ├── baichuan_completion.json
│   │   │   ├── common_chat.json
│   │   │   └── common_completion.json
│   │   ├── prompt_transform.py
│   │   ├── simple_prompt_transform.py
│   │   └── utils
│   │       ├── __init__.py
│   │       ├── prompt_message_util.py
│   │       └── prompt_template_parser.py
│   ├── provider_manager.py
│   ├── rag
│   │   ├── __init__.py
│   │   ├── cleaner
│   │   │   ├── clean_processor.py
│   │   │   ├── cleaner_base.py
│   │   │   └── unstructured
│   │   │       ├── unstructured_extra_whitespace_cleaner.py
│   │   │       ├── unstructured_group_broken_paragraphs_cleaner.py
│   │   │       ├── unstructured_non_ascii_chars_cleaner.py
│   │   │       ├── unstructured_replace_unicode_quotes_cleaner.py
│   │   │       └── unstructured_translate_text_cleaner.py
│   │   ├── data_post_processor
│   │   │   ├── __init__.py
│   │   │   ├── data_post_processor.py
│   │   │   └── reorder.py
│   │   ├── datasource
│   │   │   ├── __init__.py
│   │   │   ├── entity
│   │   │   │   └── embedding.py
│   │   │   ├── keyword
│   │   │   │   ├── __init__.py
│   │   │   │   ├── jieba
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── jieba.py
│   │   │   │   │   ├── jieba_keyword_table_handler.py
│   │   │   │   │   └── stopwords.py
│   │   │   │   ├── keyword_base.py
│   │   │   │   └── keyword_factory.py
│   │   │   ├── retrieval_service.py
│   │   │   └── vdb
│   │   │       ├── __init__.py
│   │   │       ├── field.py
│   │   │       ├── milvus
│   │   │       │   ├── __init__.py
│   │   │       │   └── milvus_vector.py
│   │   │       ├── pgvecto_rs
│   │   │       │   ├── __init__.py
│   │   │       │   ├── collection.py
│   │   │       │   └── pgvecto_rs.py
│   │   │       ├── pgvector
│   │   │       │   ├── __init__.py
│   │   │       │   └── pgvector.py
│   │   │       ├── qdrant
│   │   │       │   ├── __init__.py
│   │   │       │   └── qdrant_vector.py
│   │   │       ├── relyt
│   │   │       │   ├── __init__.py
│   │   │       │   └── relyt_vector.py
│   │   │       ├── vector_base.py
│   │   │       ├── vector_factory.py
│   │   │       └── weaviate
│   │   │           ├── __init__.py
│   │   │           └── weaviate_vector.py
│   │   ├── extractor
│   │   │   ├── blod
│   │   │   │   └── blod.py
│   │   │   ├── csv_extractor.py
│   │   │   ├── entity
│   │   │   │   ├── datasource_type.py
│   │   │   │   └── extract_setting.py
│   │   │   ├── excel_extractor.py
│   │   │   ├── extract_processor.py
│   │   │   ├── extractor_base.py
│   │   │   ├── helpers.py
│   │   │   ├── html_extractor.py
│   │   │   ├── markdown_extractor.py
│   │   │   ├── notion_extractor.py
│   │   │   ├── pdf_extractor.py
│   │   │   ├── text_extractor.py
│   │   │   ├── unstructured
│   │   │   │   ├── unstructured_doc_extractor.py
│   │   │   │   ├── unstructured_eml_extractor.py
│   │   │   │   ├── unstructured_epub_extractor.py
│   │   │   │   ├── unstructured_markdown_extractor.py
│   │   │   │   ├── unstructured_msg_extractor.py
│   │   │   │   ├── unstructured_ppt_extractor.py
│   │   │   │   ├── unstructured_pptx_extractor.py
│   │   │   │   ├── unstructured_text_extractor.py
│   │   │   │   └── unstructured_xml_extractor.py
│   │   │   └── word_extractor.py
│   │   ├── index_processor
│   │   │   ├── __init__.py
│   │   │   ├── constant
│   │   │   │   ├── __init__.py
│   │   │   │   └── index_type.py
│   │   │   ├── index_processor_base.py
│   │   │   ├── index_processor_factory.py
│   │   │   └── processor
│   │   │       ├── __init__.py
│   │   │       ├── paragraph_index_processor.py
│   │   │       └── qa_index_processor.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   └── document.py
│   │   └── retrieval
│   │       ├── __init__.py
│   │       ├── dataset_retrieval.py
│   │       ├── output_parser
│   │       │   ├── __init__.py
│   │       │   ├── react_output.py
│   │       │   └── structured_chat.py
│   │       └── router
│   │           ├── multi_dataset_function_call_router.py
│   │           └── multi_dataset_react_route.py
│   ├── rerank
│   │   ├── __init__.py
│   │   └── rerank.py
│   ├── splitter
│   │   ├── fixed_text_splitter.py
│   │   └── text_splitter.py
│   ├── tools
│   │   ├── README.md
│   │   ├── README_CN.md
│   │   ├── docs
│   │   │   ├── en_US
│   │   │   │   ├── advanced_scale_out.md
│   │   │   │   └── tool_scale_out.md
│   │   │   └── zh_Hans
│   │   │       ├── advanced_scale_out.md
│   │   │       ├── images
│   │   │       │   └── index
│   │   │       └── tool_scale_out.md
│   │   ├── entities
│   │   │   ├── common_entities.py
│   │   │   ├── constant.py
│   │   │   ├── tool_bundle.py
│   │   │   ├── tool_entities.py
│   │   │   └── user_entities.py
│   │   ├── errors.py
│   │   ├── model
│   │   │   ├── errors.py
│   │   │   └── tool_model_manager.py
│   │   ├── prompt
│   │   │   └── template.py
│   │   ├── provider
│   │   │   ├── _position.yaml
│   │   │   ├── api_tool_provider.py
│   │   │   ├── app_tool_provider.py
│   │   │   ├── builtin
│   │   │   │   ├── __init__.py
│   │   │   │   ├── _positions.py
│   │   │   │   ├── aippt
│   │   │   │   │   ├── _assets
│   │   │   │   │   ├── aippt.py
│   │   │   │   │   ├── aippt.yaml
│   │   │   │   │   └── tools
│   │   │   │   ├── arxiv
│   │   │   │   │   ├── _assets
│   │   │   │   │   ├── arxiv.py
│   │   │   │   │   ├── arxiv.yaml
│   │   │   │   │   └── tools
│   │   │   │   ├── azuredalle
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── _assets
│   │   │   │   │   ├── azuredalle.py
│   │   │   │   │   ├── azuredalle.yaml
│   │   │   │   │   └── tools
│   │   │   │   ├── bing
│   │   │   │   │   ├── _assets
│   │   │   │   │   ├── bing.py
│   │   │   │   │   ├── bing.yaml
│   │   │   │   │   └── tools
│   │   │   │   ├── brave
│   │   │   │   │   ├── _assets
│   │   │   │   │   ├── brave.py
│   │   │   │   │   ├── brave.yaml
│   │   │   │   │   └── tools
│   │   │   │   ├── chart
│   │   │   │   │   ├── _assets
│   │   │   │   │   ├── chart.py
│   │   │   │   │   ├── chart.yaml
│   │   │   │   │   └── tools
│   │   │   │   ├── code
│   │   │   │   │   ├── _assets
│   │   │   │   │   ├── code.py
│   │   │   │   │   ├── code.yaml
│   │   │   │   │   └── tools
│   │   │   │   ├── dalle
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── _assets
│   │   │   │   │   ├── dalle.py
│   │   │   │   │   ├── dalle.yaml
│   │   │   │   │   └── tools
│   │   │   │   ├── devdocs
│   │   │   │   │   ├── _assets
│   │   │   │   │   ├── devdocs.py
│   │   │   │   │   ├── devdocs.yaml
│   │   │   │   │   └── tools
│   │   │   │   ├── dingtalk
│   │   │   │   │   ├── _assets
│   │   │   │   │   ├── dingtalk.py
│   │   │   │   │   ├── dingtalk.yaml
│   │   │   │   │   └── tools
│   │   │   │   ├── duckduckgo
│   │   │   │   │   ├── _assets
│   │   │   │   │   ├── duckduckgo.py
│   │   │   │   │   ├── duckduckgo.yaml
│   │   │   │   │   └── tools
│   │   │   │   ├── feishu
│   │   │   │   │   ├── _assets
│   │   │   │   │   ├── feishu.py
│   │   │   │   │   ├── feishu.yaml
│   │   │   │   │   └── tools
│   │   │   │   ├── firecrawl
│   │   │   │   │   ├── _assets
│   │   │   │   │   ├── firecrawl.py
│   │   │   │   │   ├── firecrawl.yaml
│   │   │   │   │   └── tools
│   │   │   │   ├── gaode
│   │   │   │   │   ├── _assets
│   │   │   │   │   ├── gaode.py
│   │   │   │   │   ├── gaode.yaml
│   │   │   │   │   └── tools
│   │   │   │   ├── github
│   │   │   │   │   ├── _assets
│   │   │   │   │   ├── github.py
│   │   │   │   │   ├── github.yaml
│   │   │   │   │   └── tools
│   │   │   │   ├── google
│   │   │   │   │   ├── _assets
│   │   │   │   │   ├── google.py
│   │   │   │   │   ├── google.yaml
│   │   │   │   │   └── tools
│   │   │   │   ├── jina
│   │   │   │   │   ├── _assets
│   │   │   │   │   ├── jina.py
│   │   │   │   │   ├── jina.yaml
│   │   │   │   │   └── tools
│   │   │   │   ├── judge0ce
│   │   │   │   │   ├── _assets
│   │   │   │   │   ├── judge0ce.py
│   │   │   │   │   ├── judge0ce.yaml
│   │   │   │   │   └── tools
│   │   │   │   ├── maths
│   │   │   │   │   ├── _assets
│   │   │   │   │   ├── maths.py
│   │   │   │   │   ├── maths.yaml
│   │   │   │   │   └── tools
│   │   │   │   ├── openweather
│   │   │   │   │   ├── _assets
│   │   │   │   │   ├── openweather.py
│   │   │   │   │   ├── openweather.yaml
│   │   │   │   │   └── tools
│   │   │   │   ├── pubmed
│   │   │   │   │   ├── _assets
│   │   │   │   │   ├── pubmed.py
│   │   │   │   │   ├── pubmed.yaml
│   │   │   │   │   └── tools
│   │   │   │   ├── qrcode
│   │   │   │   │   ├── _assets
│   │   │   │   │   ├── qrcode.py
│   │   │   │   │   ├── qrcode.yaml
│   │   │   │   │   └── tools
│   │   │   │   ├── searxng
│   │   │   │   │   ├── _assets
│   │   │   │   │   ├── searxng.py
│   │   │   │   │   ├── searxng.yaml
│   │   │   │   │   └── tools
│   │   │   │   ├── slack
│   │   │   │   │   ├── _assets
│   │   │   │   │   ├── slack.py
│   │   │   │   │   ├── slack.yaml
│   │   │   │   │   └── tools
│   │   │   │   ├── spark
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── _assets
│   │   │   │   │   ├── spark.py
│   │   │   │   │   ├── spark.yaml
│   │   │   │   │   └── tools
│   │   │   │   ├── stability
│   │   │   │   │   ├── _assets
│   │   │   │   │   ├── stability.py
│   │   │   │   │   ├── stability.yaml
│   │   │   │   │   └── tools
│   │   │   │   ├── stablediffusion
│   │   │   │   │   ├── _assets
│   │   │   │   │   ├── stablediffusion.py
│   │   │   │   │   ├── stablediffusion.yaml
│   │   │   │   │   └── tools
│   │   │   │   ├── stackexchange
│   │   │   │   │   ├── _assets
│   │   │   │   │   ├── stackexchange.py
│   │   │   │   │   ├── stackexchange.yaml
│   │   │   │   │   └── tools
│   │   │   │   ├── tavily
│   │   │   │   │   ├── _assets
│   │   │   │   │   ├── tavily.py
│   │   │   │   │   ├── tavily.yaml
│   │   │   │   │   └── tools
│   │   │   │   ├── time
│   │   │   │   │   ├── _assets
│   │   │   │   │   ├── time.py
│   │   │   │   │   ├── time.yaml
│   │   │   │   │   └── tools
│   │   │   │   ├── trello
│   │   │   │   │   ├── _assets
│   │   │   │   │   ├── tools
│   │   │   │   │   ├── trello.py
│   │   │   │   │   └── trello.yaml
│   │   │   │   ├── twilio
│   │   │   │   │   ├── _assets
│   │   │   │   │   ├── tools
│   │   │   │   │   ├── twilio.py
│   │   │   │   │   └── twilio.yaml
│   │   │   │   ├── vectorizer
│   │   │   │   │   ├── _assets
│   │   │   │   │   ├── tools
│   │   │   │   │   ├── vectorizer.py
│   │   │   │   │   └── vectorizer.yaml
│   │   │   │   ├── webscraper
│   │   │   │   │   ├── _assets
│   │   │   │   │   ├── tools
│   │   │   │   │   ├── webscraper.py
│   │   │   │   │   └── webscraper.yaml
│   │   │   │   ├── wecom
│   │   │   │   │   ├── _assets
│   │   │   │   │   ├── tools
│   │   │   │   │   ├── wecom.py
│   │   │   │   │   └── wecom.yaml
│   │   │   │   ├── wikipedia
│   │   │   │   │   ├── _assets
│   │   │   │   │   ├── tools
│   │   │   │   │   ├── wikipedia.py
│   │   │   │   │   └── wikipedia.yaml
│   │   │   │   ├── wolframalpha
│   │   │   │   │   ├── _assets
│   │   │   │   │   ├── tools
│   │   │   │   │   ├── wolframalpha.py
│   │   │   │   │   └── wolframalpha.yaml
│   │   │   │   ├── yahoo
│   │   │   │   │   ├── _assets
│   │   │   │   │   ├── tools
│   │   │   │   │   ├── yahoo.py
│   │   │   │   │   └── yahoo.yaml
│   │   │   │   └── youtube
│   │   │   │       ├── _assets
│   │   │   │       ├── tools
│   │   │   │       ├── youtube.py
│   │   │   │       └── youtube.yaml
│   │   │   ├── builtin_tool_provider.py
│   │   │   └── tool_provider.py
│   │   ├── tool
│   │   │   ├── api_tool.py
│   │   │   ├── builtin_tool.py
│   │   │   ├── dataset_retriever
│   │   │   │   ├── dataset_multi_retriever_tool.py
│   │   │   │   ├── dataset_retriever_base_tool.py
│   │   │   │   └── dataset_retriever_tool.py
│   │   │   ├── dataset_retriever_tool.py
│   │   │   └── tool.py
│   │   ├── tool_engine.py
│   │   ├── tool_file_manager.py
│   │   ├── tool_manager.py
│   │   └── utils
│   │       ├── configuration.py
│   │       ├── message_transformer.py
│   │       ├── parser.py
│   │       ├── uuid_utils.py
│   │       └── web_reader_tool.py
│   ├── utils
│   │   ├── module_import_helper.py
│   │   └── position_helper.py
│   └── workflow
│       ├── __init__.py
│       ├── callbacks
│       │   ├── __init__.py
│       │   └── base_workflow_callback.py
│       ├── entities
│       │   ├── __init__.py
│       │   ├── base_node_data_entities.py
│       │   ├── node_entities.py
│       │   ├── variable_entities.py
│       │   ├── variable_pool.py
│       │   └── workflow_entities.py
│       ├── errors.py
│       ├── nodes
│       │   ├── __init__.py
│       │   ├── answer
│       │   │   ├── __init__.py
│       │   │   ├── answer_node.py
│       │   │   └── entities.py
│       │   ├── base_node.py
│       │   ├── code
│       │   │   ├── __init__.py
│       │   │   ├── code_node.py
│       │   │   └── entities.py
│       │   ├── end
│       │   │   ├── __init__.py
│       │   │   ├── end_node.py
│       │   │   └── entities.py
│       │   ├── http_request
│       │   │   ├── __init__.py
│       │   │   ├── entities.py
│       │   │   ├── http_executor.py
│       │   │   └── http_request_node.py
│       │   ├── if_else
│       │   │   ├── __init__.py
│       │   │   ├── entities.py
│       │   │   └── if_else_node.py
│       │   ├── knowledge_retrieval
│       │   │   ├── __init__.py
│       │   │   ├── entities.py
│       │   │   └── knowledge_retrieval_node.py
│       │   ├── llm
│       │   │   ├── __init__.py
│       │   │   ├── entities.py
│       │   │   └── llm_node.py
│       │   ├── question_classifier
│       │   │   ├── __init__.py
│       │   │   ├── entities.py
│       │   │   ├── question_classifier_node.py
│       │   │   └── template_prompts.py
│       │   ├── start
│       │   │   ├── __init__.py
│       │   │   ├── entities.py
│       │   │   └── start_node.py
│       │   ├── template_transform
│       │   │   ├── __init__.py
│       │   │   ├── entities.py
│       │   │   └── template_transform_node.py
│       │   ├── tool
│       │   │   ├── __init__.py
│       │   │   ├── entities.py
│       │   │   └── tool_node.py
│       │   └── variable_assigner
│       │       ├── __init__.py
│       │       ├── entities.py
│       │       └── variable_assigner_node.py
│       ├── utils
│       │   ├── __init__.py
│       │   └── variable_template_parser.py
│       └── workflow_engine_manager.py
├── docker
│   └── entrypoint.sh
├── events
│   ├── app_event.py
│   ├── dataset_event.py
│   ├── document_event.py
│   ├── event_handlers
│   │   ├── __init__.py
│   │   ├── clean_when_dataset_deleted.py
│   │   ├── clean_when_document_deleted.py
│   │   ├── create_document_index.py
│   │   ├── create_installed_app_when_app_created.py
│   │   ├── create_site_record_when_app_created.py
│   │   ├── deduct_quota_when_messaeg_created.py
│   │   ├── delete_installed_app_when_app_deleted.py
│   │   ├── delete_tool_parameters_cache_when_sync_draft_workflow.py
│   │   ├── document_index_event.py
│   │   ├── update_app_dataset_join_when_app_model_config_updated.py
│   │   ├── update_app_dataset_join_when_app_published_workflow_updated.py
│   │   └── update_provider_last_used_at_when_messaeg_created.py
│   ├── message_event.py
│   └── tenant_event.py
├── extensions
│   ├── ext_celery.py
│   ├── ext_code_based_extension.py
│   ├── ext_compress.py
│   ├── ext_database.py
│   ├── ext_hosting_provider.py
│   ├── ext_login.py
│   ├── ext_mail.py
│   ├── ext_migrate.py
│   ├── ext_redis.py
│   ├── ext_sentry.py
│   ├── ext_storage.py
│   └── storage
│       ├── aliyun_storage.py
│       ├── azure_storage.py
│       ├── base_storage.py
│       ├── google_storage.py
│       ├── local_storage.py
│       └── s3_storage.py
├── fields
│   ├── __init__.py
│   ├── annotation_fields.py
│   ├── api_based_extension_fields.py
│   ├── app_fields.py
│   ├── conversation_fields.py
│   ├── data_source_fields.py
│   ├── dataset_fields.py
│   ├── document_fields.py
│   ├── end_user_fields.py
│   ├── file_fields.py
│   ├── hit_testing_fields.py
│   ├── installed_app_fields.py
│   ├── member_fields.py
│   ├── message_fields.py
│   ├── segment_fields.py
│   ├── tag_fields.py
│   ├── workflow_app_log_fields.py
│   ├── workflow_fields.py
│   └── workflow_run_fields.py
├── libs
│   ├── __init__.py
│   ├── exception.py
│   ├── external_api.py
│   ├── gmpy2_pkcs10aep_cipher.py
│   ├── helper.py
│   ├── infinite_scroll_pagination.py
│   ├── json_in_md_parser.py
│   ├── login.py
│   ├── oauth.py
│   ├── oauth_data_source.py
│   ├── passport.py
│   ├── password.py
│   ├── rsa.py
│   └── smtp.py
├── mabos
│   ├── agents
│   │   └── {agent_id}
│   │       ├── communication_api.py
│   │       ├── execution_api.py
│   │       ├── plans_api.py
│   │       └── reasoning_api.py
│   ├── agents_api.py
│   ├── knowledge-graph_api.py
│   └── ontologies_api.py
├── migrations
│   ├── README
│   ├── alembic.ini
│   ├── env.py
│   ├── script.py.mako
│   └── versions
│       ├── 00bacef91f18_rename_api_provider_description.py
│       ├── 053da0c1d756_add_api_tool_privacy.py
│       ├── 114eed84c228_remove_tool_id_from_model_invoke.py
│       ├── 16830a790f0f_.py
│       ├── 16fa53d9faec_add_provider_model_support.py
│       ├── 17b5ab037c40_add_keyworg_table_storage_type.py
│       ├── 187385f442fc_modify_provider_model_name_length.py
│       ├── 23db93619b9d_add_message_files_into_agent_thought.py
│       ├── 246ba09cbbdb_add_app_anntation_setting.py
│       ├── 2beac44e5f5f_add_is_universal_in_apps.py
│       ├── 2c8af9671032_add_qa_document_language.py
│       ├── 2e9819ca5b28_add_tenant_id_in_api_token.py
│       ├── 380c6aa5a70d_add_tool_labels_to_agent_thought.py
│       ├── 3c7cac9521c6_add_tags_and_binding_table.py
│       ├── 3ef9b2b6bee6_add_assistant_app.py
│       ├── 42e85ed5564d_conversation_columns_set_nullable.py
│       ├── 46976cc39132_add_annotation_histoiry_score.py
│       ├── 47cc7df8c4f3_modify_default_model_name_length.py
│       ├── 4823da1d26cf_add_tool_file.py
│       ├── 4829e54d2fee_change_message_chain_id_to_nullable.py
│       ├── 4bcffcd64aa4_update_dataset_model_field_null_.py
│       ├── 5022897aaceb_add_model_name_in_embedding.py
│       ├── 563cf8bf777b_enable_tool_file_without_conversation_id.py
│       ├── 614f77cecc48_add_last_active_at.py
│       ├── 64b051264f32_init.py
│       ├── 6dcb43972bdc_add_dataset_retriever_resource.py
│       ├── 6e2cfb077b04_add_dataset_collection_binding.py
│       ├── 714aafe25d39_add_anntation_history_match_response.py
│       ├── 77e83833755c_add_app_config_retriever_resource.py
│       ├── 7ce5a52e4eee_add_tool_providers.py
│       ├── 853f9b9cd3b6_add_message_price_unit.py
│       ├── 88072f0caa04_add_custom_config_in_tenant.py
│       ├── 89c7899ca936_.py
│       ├── 8ae9bc661daa_add_tool_conversation_variables_idx.py
│       ├── 8d2d099ceb74_add_qa_model_support.py
│       ├── 8ec536f3c800_rename_api_provider_credentails.py
│       ├── 8fe468ba0ca5_add_gpt4v_supports.py
│       ├── 968fff4c0ab9_add_api_based_extension.py
│       ├── 9f4e3427ea84_add_created_by_role.py
│       ├── 9fafbd60eca1_add_message_file_belongs_to.py
│       ├── a45f4dfde53b_add_language_to_recommend_apps.py
│       ├── a5b56fb053ef_app_config_add_speech_to_text.py
│       ├── a8d7385a7b66_add_embeddings_provider_name.py
│       ├── a8f9b3c45e4a_add_tenant_id_db_index.py
│       ├── a9836e3baeee_add_external_data_tools_in_app_model_.py
│       ├── ab23c11305d4_add_dataset_query_variable_at_app_model_.py
│       ├── ad472b61a054_add_api_provider_icon.py
│       ├── b24be59fbb04_.py
│       ├── b289e2408ee2_add_workflow.py
│       ├── b3a09c049e8e_add_advanced_prompt_templates.py
│       ├── b5429b71023c_messages_columns_set_nullable.py
│       ├── bf0aec5ba2cf_add_provider_order.py
│       ├── c3311b089690_add_tool_meta.py
│       ├── c71211c8f604_add_tool_invoke_model_log.py
│       ├── cc04d0998d4d_set_model_config_column_nullable.py
│       ├── d3d503a3471c_add_is_deleted_to_conversations.py
│       ├── de95f5c77138_migration_serpapi_api_key.py
│       ├── dfb3b7f477da_add_tool_index.py
│       ├── e1901f623fd0_add_annotation_reply.py
│       ├── e2eacc9a1b63_add_status_for_message.py
│       ├── e32f6ccb87c6_e08af0a69ccefbb59fa80c778efee300bb780980.py
│       ├── e35ed59becda_modify_quota_limit_field_type.py
│       ├── e8883b0148c9_add_dataset_model_name.py
│       ├── f25003750af4_add_created_updated_at.py
│       ├── f2a6fc85e260_add_anntation_history_message_id.py
│       ├── f9107f83abab_add_desc_for_apps.py
│       └── fca025d3b60f_add_dataset_retrival_model.py
├── models
│   ├── __init__.py
│   ├── account.py
│   ├── api_based_extension.py
│   ├── dataset.py
│   ├── mabos
│   │   ├── __init__.py
│   │   ├── agent.py
│   │   ├── communication.py
│   │   ├── execution.py
│   │   ├── knowledge_graph.py
│   │   ├── ontology_api.py
│   │   ├── planning.py
│   │   └── reasoning.py
│   ├── model.py
│   ├── provider.py
│   ├── source.py
│   ├── task.py
│   ├── tool.py
│   ├── tools.py
│   ├── web.py
│   └── workflow.py
├── pyproject.toml
├── requirements-dev.txt
├── requirements.txt
├── routers
│   └── mabos.py
├── schedule
│   ├── clean_embedding_cache_task.py
│   └── clean_unused_datasets_task.py
├── services
│   ├── __init__.py
│   ├── account_service.py
│   ├── advanced_prompt_template_service.py
│   ├── agent_service.py
│   ├── annotation_service.py
│   ├── api_based_extension_service.py
│   ├── app_generate_service.py
│   ├── app_model_config_service.py
│   ├── app_service.py
│   ├── audio_service.py
│   ├── billing_service.py
│   ├── code_based_extension_service.py
│   ├── conversation_service.py
│   ├── dataset_service.py
│   ├── enterprise
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── enterprise_service.py
│   ├── entities
│   │   ├── __init__.py
│   │   └── model_provider_entities.py
│   ├── errors
│   │   ├── __init__.py
│   │   ├── account.py
│   │   ├── app.py
│   │   ├── app_model_config.py
│   │   ├── audio.py
│   │   ├── base.py
│   │   ├── completion.py
│   │   ├── conversation.py
│   │   ├── dataset.py
│   │   ├── document.py
│   │   ├── file.py
│   │   ├── index.py
│   │   └── message.py
│   ├── feature_service.py
│   ├── file_service.py
│   ├── hit_testing_service.py
│   ├── mabos_service.py
│   ├── message_service.py
│   ├── model_provider_service.py
│   ├── moderation_service.py
│   ├── operation_service.py
│   ├── recommended_app_service.py
│   ├── saved_message_service.py
│   ├── tag_service.py
│   ├── tools_manage_service.py
│   ├── tools_transform_service.py
│   ├── vector_service.py
│   ├── web_conversation_service.py
│   ├── workflow
│   │   ├── __init__.py
│   │   └── workflow_converter.py
│   ├── workflow_app_service.py
│   ├── workflow_run_service.py
│   ├── workflow_service.py
│   └── workspace_service.py
├── tasks
│   ├── add_document_to_index_task.py
│   ├── annotation
│   │   ├── add_annotation_to_index_task.py
│   │   ├── batch_import_annotations_task.py
│   │   ├── delete_annotation_index_task.py
│   │   ├── disable_annotation_reply_task.py
│   │   ├── enable_annotation_reply_task.py
│   │   └── update_annotation_to_index_task.py
│   ├── batch_create_segment_to_index_task.py
│   ├── clean_dataset_task.py
│   ├── clean_document_task.py
│   ├── clean_notion_document_task.py
│   ├── create_segment_to_index_task.py
│   ├── deal_dataset_vector_index_task.py
│   ├── delete_segment_from_index_task.py
│   ├── disable_segment_from_index_task.py
│   ├── document_indexing_sync_task.py
│   ├── document_indexing_task.py
│   ├── document_indexing_update_task.py
│   ├── duplicate_document_indexing_task.py
│   ├── enable_segment_to_index_task.py
│   ├── mail_invite_member_task.py
│   ├── recover_document_indexing_task.py
│   ├── remove_document_from_index_task.py
│   └── retry_document_indexing_task.py
├── templates
│   ├── invite_member_mail_template_en-US.html
│   └── invite_member_mail_template_zh-CN.html
└── tests
    ├── __init__.py
    ├── integration_tests
    │   ├── __init__.py
    │   ├── conftest.py
    │   ├── model_runtime
    │   │   ├── __init__.py
    │   │   ├── __mock
    │   │   │   ├── anthropic.py
    │   │   │   ├── google.py
    │   │   │   ├── huggingface.py
    │   │   │   ├── huggingface_chat.py
    │   │   │   ├── openai.py
    │   │   │   ├── openai_chat.py
    │   │   │   ├── openai_completion.py
    │   │   │   ├── openai_embeddings.py
    │   │   │   ├── openai_moderation.py
    │   │   │   ├── openai_remote.py
    │   │   │   ├── openai_speech2text.py
    │   │   │   └── xinference.py
    │   │   ├── anthropic
    │   │   │   ├── __init__.py
    │   │   │   ├── test_llm.py
    │   │   │   └── test_provider.py
    │   │   ├── assets
    │   │   │   └── audio.mp3
    │   │   ├── azure_openai
    │   │   │   ├── __init__.py
    │   │   │   ├── test_llm.py
    │   │   │   └── test_text_embedding.py
    │   │   ├── baichuan
    │   │   │   ├── __init__.py
    │   │   │   ├── test_llm.py
    │   │   │   ├── test_provider.py
    │   │   │   └── test_text_embedding.py
    │   │   ├── bedrock
    │   │   │   ├── __init__.py
    │   │   │   ├── test_llm.py
    │   │   │   └── test_provider.py
    │   │   ├── chatglm
    │   │   │   ├── __init__.py
    │   │   │   ├── test_llm.py
    │   │   │   └── test_provider.py
    │   │   ├── cohere
    │   │   │   ├── __init__.py
    │   │   │   ├── test_llm.py
    │   │   │   ├── test_provider.py
    │   │   │   ├── test_rerank.py
    │   │   │   └── test_text_embedding.py
    │   │   ├── google
    │   │   │   ├── __init__.py
    │   │   │   ├── test_llm.py
    │   │   │   └── test_provider.py
    │   │   ├── huggingface_hub
    │   │   │   ├── __init__.py
    │   │   │   ├── test_llm.py
    │   │   │   └── test_text_embedding.py
    │   │   ├── jina
    │   │   │   ├── __init__.py
    │   │   │   ├── test_provider.py
    │   │   │   └── test_text_embedding.py
    │   │   ├── localai
    │   │   │   ├── __init__.py
    │   │   │   ├── test_embedding.py
    │   │   │   ├── test_llm.py
    │   │   │   ├── test_rerank.py
    │   │   │   └── test_speech2text.py
    │   │   ├── minimax
    │   │   │   ├── __init__.py
    │   │   │   ├── test_embedding.py
    │   │   │   ├── test_llm.py
    │   │   │   └── test_provider.py
    │   │   ├── ollama
    │   │   │   ├── __init__.py
    │   │   │   ├── test_llm.py
    │   │   │   └── test_text_embedding.py
    │   │   ├── openai
    │   │   │   ├── __init__.py
    │   │   │   ├── test_llm.py
    │   │   │   ├── test_moderation.py
    │   │   │   ├── test_provider.py
    │   │   │   ├── test_speech2text.py
    │   │   │   └── test_text_embedding.py
    │   │   ├── openai_api_compatible
    │   │   │   ├── __init__.py
    │   │   │   ├── test_llm.py
    │   │   │   └── test_text_embedding.py
    │   │   ├── openllm
    │   │   │   ├── __init__.py
    │   │   │   ├── test_embedding.py
    │   │   │   └── test_llm.py
    │   │   ├── openrouter
    │   │   │   ├── __init__.py
    │   │   │   └── test_llm.py
    │   │   ├── replicate
    │   │   │   ├── __init__.py
    │   │   │   ├── test_llm.py
    │   │   │   └── test_text_embedding.py
    │   │   ├── spark
    │   │   │   ├── __init__.py
    │   │   │   ├── test_llm.py
    │   │   │   └── test_provider.py
    │   │   ├── test_model_provider_factory.py
    │   │   ├── togetherai
    │   │   │   ├── __init__.py
    │   │   │   └── test_llm.py
    │   │   ├── tongyi
    │   │   │   ├── __init__.py
    │   │   │   ├── test_llm.py
    │   │   │   └── test_provider.py
    │   │   ├── volcengine_maas
    │   │   │   ├── __init__.py
    │   │   │   ├── test_embedding.py
    │   │   │   └── test_llm.py
    │   │   ├── wenxin
    │   │   │   ├── __init__.py
    │   │   │   ├── test_llm.py
    │   │   │   └── test_provider.py
    │   │   ├── xinference
    │   │   │   ├── __init__.py
    │   │   │   ├── test_embeddings.py
    │   │   │   ├── test_llm.py
    │   │   │   └── test_rerank.py
    │   │   └── zhipuai
    │   │       ├── __init__.py
    │   │       ├── test_llm.py
    │   │       ├── test_provider.py
    │   │       └── test_text_embedding.py
    │   ├── tools
    │   │   ├── __init__.py
    │   │   ├── __mock_server
    │   │   │   └── openapi_todo.py
    │   │   ├── code
    │   │   │   └── __init__.py
    │   │   └── test_all_provider.py
    │   ├── utils
    │   │   ├── child_class.py
    │   │   ├── lazy_load_class.py
    │   │   ├── parent_class.py
    │   │   └── test_module_import_helper.py
    │   ├── vdb
    │   │   ├── __init__.py
    │   │   ├── milvus
    │   │   │   ├── __init__.py
    │   │   │   └── test_milvus.py
    │   │   ├── pgvecto_rs
    │   │   │   ├── __init__.py
    │   │   │   └── test_pgvecto_rs.py
    │   │   ├── pgvector
    │   │   │   ├── __init__.py
    │   │   │   └── test_pgvector.py
    │   │   ├── qdrant
    │   │   │   ├── __init__.py
    │   │   │   └── test_qdrant.py
    │   │   ├── test_vector_store.py
    │   │   └── weaviate
    │   │       ├── __init__.py
    │   │       └── test_weaviate.py
    │   └── workflow
    │       ├── __init__.py
    │       └── nodes
    │           ├── __init__.py
    │           ├── __mock
    │           │   ├── code_executor.py
    │           │   └── http.py
    │           ├── code_executor
    │           │   ├── __init__.py
    │           │   ├── test_code_executor.py
    │           │   ├── test_code_javascript.py
    │           │   ├── test_code_jinja2.py
    │           │   └── test_code_python3.py
    │           ├── test_code.py
    │           ├── test_http.py
    │           ├── test_llm.py
    │           ├── test_template_transform.py
    │           └── test_tool.py
    └── unit_tests
        ├── __init__.py
        ├── conftest.py
        ├── core
        │   ├── __init__.py
        │   ├── prompt
        │   │   ├── __init__.py
        │   │   ├── test_advanced_prompt_transform.py
        │   │   ├── test_prompt_transform.py
        │   │   └── test_simple_prompt_transform.py
        │   ├── rag
        │   │   ├── __init__.py
        │   │   └── datasource
        │   │       ├── __init__.py
        │   │       └── vdb
        │   └── workflow
        │       ├── __init__.py
        │       └── nodes
        │           ├── __init__.py
        │           ├── test_answer.py
        │           └── test_if_else.py
        ├── libs
        │   ├── test_rsa.py
        │   └── test_yarl.py
        ├── models
        │   └── test_account.py
        └── services
            ├── __init__.py
            └── workflow
                ├── __init__.py
                └── test_workflow_converter.py