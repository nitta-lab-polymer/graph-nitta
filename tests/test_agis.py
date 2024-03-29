from pathlib import Path

import pandas as pd
from graph_nitta import AxConfig, SpineConfig, apply_ax_config, make_graph
from matplotlib.testing.decorators import image_comparison


@image_comparison(baseline_images=["agis"], extensions=["png"], style="mpl20")
def test_agis():
    base_path = Path(__file__).parent.parent
    df = pd.read_csv(f"{base_path}/sample_data/agis.csv", index_col=0)

    # グラフ作成
    fig, axes = make_graph()

    # グラフにデータを追加
    axes[0].plot(df[df.columns[0]], df[df.columns[1]], label="sample1")
    axes[0].plot(df[df.columns[0]] * 1.1, df[df.columns[1]] * 1.1, label="sample2")

    # グラフの設定
    config = AxConfig(
        x=SpineConfig(lim=(0, 5)),
        y=SpineConfig(lim=(0, 1)),
        is_visible_legend=False,
    )
    apply_ax_config(axes[0], config)
