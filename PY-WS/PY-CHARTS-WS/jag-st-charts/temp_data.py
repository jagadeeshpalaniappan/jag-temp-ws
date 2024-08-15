import uuid

template = {
    "tabs": [
        {
            "name": "Tab 1",
            "charts": [
                {
                    "name": "Chart 1",
                    "tags": [
                        {"name": "Tag A", "id": "temp_min", "type": "ASSET_TAG"},
                        {"name": "Tag B", "id": "temp_max", "type": "ASSET_TAG"},
                        {"name": "Tag C", "id": "wind", "type": "ASSET_TAG"},
                    ],
                },
                {
                    "name": "Chart 2",
                    "tags": [
                        {"name": "Tag A", "id": "temp_min", "type": "ASSET_TAG"},
                        {"name": "Tag B", "id": "temp_max", "type": "ASSET_TAG"},
                        {"name": "Tag C", "id": "wind", "type": "ASSET_TAG"},
                    ],
                },
                {
                    "name": "Chart 3",
                    "tags": [
                        {"name": "Tag A", "id": "temp_min", "type": "ASSET_TAG"},
                        {"name": "Tag B", "id": "temp_max", "type": "ASSET_TAG"},
                        {"name": "Tag C", "id": "wind", "type": "ASSET_TAG"},
                    ],
                },
                {
                    "name": "Chart 4",
                    "tags": [
                        {"name": "Tag A", "id": "temp_min", "type": "ASSET_TAG"},
                        {"name": "Tag B", "id": "temp_max", "type": "ASSET_TAG"},
                        {"name": "Tag C", "id": "wind", "type": "ASSET_TAG"},
                    ],
                },
                {
                    "name": "Chart 5",
                    "tags": [
                        {"name": "Tag A", "id": "temp_min", "type": "ASSET_TAG"},
                        {"name": "Tag B", "id": "temp_max", "type": "ASSET_TAG"},
                        {"name": "Tag C", "id": "wind", "type": "ASSET_TAG"},
                    ],
                },
            ],
        },
        {
            "name": "Tab 2",
            "charts": [
                {
                    "name": "Chart 1",
                    "tags": [
                        {"name": "Tag A", "id": "temp_min", "type": "ASSET_TAG"},
                        {"name": "Tag B", "id": "temp_max", "type": "ASSET_TAG"},
                        {"name": "Tag C", "id": "wind", "type": "ASSET_TAG"},
                    ],
                },
                {
                    "name": "Chart 2",
                    "tags": [
                        {"name": "Tag A", "id": "temp_min", "type": "ASSET_TAG"},
                        {"name": "Tag B", "id": "temp_max", "type": "ASSET_TAG"},
                        {"name": "Tag C", "id": "wind", "type": "ASSET_TAG"},
                    ],
                },
            ],
        },
        {
            "name": "Tab 3",
            "charts": [
                {
                    "name": "Chart 1",
                    "tags": [
                        {"name": "Tag A", "id": "temp_min", "type": "ASSET_TAG"},
                        {"name": "Tag B", "id": "temp_max", "type": "ASSET_TAG"},
                        {"name": "Tag C", "id": "wind", "type": "ASSET_TAG"},
                    ],
                },
                {
                    "name": "Chart 2",
                    "tags": [
                        {"name": "Tag A", "id": "temp_min", "type": "ASSET_TAG"},
                        {"name": "Tag B", "id": "temp_max", "type": "ASSET_TAG"},
                        {"name": "Tag C", "id": "wind", "type": "ASSET_TAG"},
                    ],
                },
                {
                    "name": "Chart 3",
                    "tags": [
                        {"name": "Tag A", "id": "temp_min", "type": "ASSET_TAG"},
                        {"name": "Tag B", "id": "temp_max", "type": "ASSET_TAG"},
                        {"name": "Tag C", "id": "wind", "type": "ASSET_TAG"},
                    ],
                },
            ],
        },
        {
            "name": "Tab 4",
            "charts": [
                {
                    "name": "Chart 1",
                    "tags": [
                        {"name": "Tag A", "id": "temp_min", "type": "ASSET_TAG"},
                        {"name": "Tag B", "id": "temp_max", "type": "ASSET_TAG"},
                        {"name": "Tag C", "id": "wind", "type": "ASSET_TAG"},
                    ],
                },
            ],
        },
    ]
}

selectedAssetIds = ["asset1", "asset2", "asset3"]

assetMap = {
    "asset1": {
        "id": uuid.uuid4(),
        "name": "Asset 1",
        "tags": [
            {
                "id": uuid.uuid4(),
                "name": "Tag A",
                "id": "temp_min",
                "type": "ASSET_TAG",
            },
            {
                "id": uuid.uuid4(),
                "name": "Tag B",
                "id": "temp_max",
                "type": "ASSET_TAG",
            },
            {"id": uuid.uuid4(), "name": "Tag C", "id": "wind", "type": "ASSET_TAG"},
            {"id": uuid.uuid4(), "name": "Tag D", "id": "tag_d", "type": "ASSET_TAG"},
            {"id": uuid.uuid4(), "name": "Tag E", "id": "tag_e", "type": "ASSET_TAG"},
            {"id": uuid.uuid4(), "name": "Tag F", "id": "tag_f", "type": "ASSET_TAG"},
        ],
    },
    "asset2": {
        "id": uuid.uuid4(),
        "name": "Asset 2",
        "tags": [
            {
                "id": uuid.uuid4(),
                "name": "Tag A",
                "id": "temp_min",
                "type": "ASSET_TAG",
            },
            {
                "id": uuid.uuid4(),
                "name": "Tag B",
                "id": "temp_max",
                "type": "ASSET_TAG",
            },
        ],
    },
    "asset3": {
        "id": uuid.uuid4(),
        "name": "Asset 3",
        "tags": [
            {
                "id": uuid.uuid4(),
                "name": "Tag A",
                "id": "temp_min",
                "type": "ASSET_TAG",
            },
            {
                "id": uuid.uuid4(),
                "name": "Tag B",
                "id": "temp_max",
                "type": "ASSET_TAG",
            },
            {"id": uuid.uuid4(), "name": "Tag C", "id": "wind", "type": "ASSET_TAG"},
        ],
    },
}
