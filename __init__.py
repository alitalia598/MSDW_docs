"""MSSDK 是基于 Python 的为麦思多维科技客户服务的专用 API 接口"""

"""
0.0.1: 发布测试版本 v0.0.1
0.0.2: 发布测试版本 v0.0.2
0.0.3: 发布测试版本 v0.0.3
0.0.4: 发布测试版本 v0.0.4
0.0.5: 发布测试版本 v0.0.5
0.0.6: 发布测试版本 v0.0.6
0.0.7: 发布测试版本 v0.0.7
0.0.8: 发布测试版本 v0.0.8
"""

__version__ = '0.0.8'
__author__ = 'mssdk'

import sys

if sys.version_info < (3, 7):
    print(f"AkShare {__version__} requires Python 3.7+")
    sys.exit(1)

del sys

"""
银行-全球银行排名
"""
from mssdk.bank.bank_banker import bank_rank_banker

"""
债券概览
"""
from mssdk.bond.bond_summary import bond_deal_summary_sse

"""
新闻-个股新闻
"""
from mssdk.news.stock_news import stock_news_em

"""
股票数据-一致行动人
"""
from mssdk.stock_feature.stock_em_yzxdr import stock_em_yzxdr

"""
大宗交易
"""
from mssdk.stock.stock_dzjy import stock_dzjy_sctj, stock_dzjy_mrmx, stock_dzjy_mrtj, stock_dzjy_hygtj, stock_dzjy_yybph, stock_dzjy_hyyybtj

"""
国证指数
"""
from mssdk.index.index_cni import index_cni_hist, index_cni_all, index_cni_detail, index_cni_detail_hist, index_cni_detail_hist_adjust

"""
金十数据-新闻资讯
"""
from mssdk.ws.js_ws_news import js_news

"""
东方财富-期权
"""
from mssdk.option.option_em import option_current_em

"""
科创板报告
"""
from mssdk.stock.zh_stock_kcb_report import zh_stock_kcb_report

"""
期货合约详情
"""
from mssdk.futures.futures_contract_detail import futures_contract_detail

"""
胡润排行榜
"""
from mssdk.fortune.hurun import hurun_rank

"""
新财富富豪榜
"""
from mssdk.fortune.xincaifu_500 import xincaifu_rank

"""
福布斯中国榜单
"""
from mssdk.fortune.forbes_500 import forbes_rank

"""
回购定盘利率
"""
from mssdk.rate.repo_rate import repo_rate_hist

"""
公募基金排行
"""
from mssdk.fund.fund_em_rank import (
    fund_em_exchange_rank,
    fund_em_money_rank,
    fund_em_open_fund_rank,
    fund_em_hk_rank,
    fund_em_lcx_rank,
)

"""
英为财情-加密货币
"""
from mssdk.crypto.crypto_hist_investing import crypto_hist, crypto_name_map

"""
电影票房
"""
from mssdk.movie.movie_yien import (
    movie_boxoffice_cinema_daily,
    movie_boxoffice_cinema_weekly,
    movie_boxoffice_weekly,
    movie_boxoffice_daily,
    movie_boxoffice_monthly,
    movie_boxoffice_realtime,
    movie_boxoffice_yearly,
    movie_boxoffice_yearly_first_week,
)

"""
新闻联播文字稿
"""
from mssdk.news.cctv_news import news_cctv

"""
债券收盘收益率曲线历史数据
"""
from mssdk.bond.bond_china_money import (
    bond_china_close_return,
    bond_china_close_return_map,
)

"""
COMEX黄金-白银库存
"""
from mssdk.futures.futures_comex import futures_comex_inventory

"""
国债期货可交割券相关指标
"""
from mssdk.bond.bond_futures import bond_futures_deliverable_coupons

"""
A 股-次新股
"""
from mssdk.stock.stock_zh_a_new import stock_zh_a_new

"""
东方财富-注册制审核
"""
from mssdk.stock_fundamental.stock_register import (
    stock_register_kcb,
    stock_register_cyb,
)

"""
新浪财经-龙虎榜
"""
from mssdk.stock_feature.stock_sina_lhb import (
    stock_sina_lhb_detail_daily,
    stock_sina_lhb_ggtj,
    stock_sina_lhb_jgmx,
    stock_sina_lhb_jgzz,
    stock_sina_lhb_yytj,
)

"""
中证指数
"""
from mssdk.index.zh_stock_index_csindex import stock_zh_index_hist_csindex

"""
股票基金持仓数据
"""
from mssdk.stock.stock_fund_hold import stock_report_fund_hold

"""
期货分钟数据
"""
from mssdk.futures.futures_zh_sina import futures_zh_minute_sina

"""
股票财务报告预约披露
"""
from mssdk.stock_feature.stock_cninfo_yjyg import stock_report_disclosure

"""
基金行情
"""
from mssdk.fund.fund_etf import fund_etf_hist_sina, fund_etf_category_sina

"""
交易日历
"""
from mssdk.tool.trade_date_hist import tool_trade_date_hist_sina

"""
commodity option
"""
from mssdk.option.option_commodity_sina import (
    option_sina_commodity_contract_list,
    option_sina_commodity_dict,
    option_sina_commodity_hist,
)

"""
A 股PE和PB
"""
from mssdk.stock_feature.stock_a_pb import stock_a_pb
from mssdk.stock_feature.stock_a_pe import stock_a_pe
from mssdk.stock_feature.stock_a_indicator import (
    stock_a_lg_indicator,
    stock_hk_eniu_indicator,
)
from mssdk.stock_feature.stock_a_high_low import stock_a_high_low_statistics
from mssdk.stock_feature.stock_a_below_net_asset_statistics import (
    stock_a_below_net_asset_statistics,
)

"""
彭博亿万富豪指数
"""
from mssdk.fortune.fortune_bloomberg import index_bloomberg_billionaires

"""
stock-券商业绩月报
"""
from mssdk.stock_feature.stock_em_qsjy import stock_em_qsjy

"""
futures-warehouse-receipt
"""
from mssdk.futures.futures_warehouse_receipt import (
    futures_czce_warehouse_receipt,
    futures_dce_warehouse_receipt,
    futures_shfe_warehouse_receipt,
)

"""
stock-js
"""
from mssdk.stock.stock_js_us import stock_js_price

"""
stock-summary
"""
from mssdk.stock.stock_summary import stock_sse_summary, stock_szse_summary

"""
股票-机构推荐池
"""
from mssdk.stock_fundamental.stock_recommend import (
    stock_institute_recommend,
    stock_institute_recommend_detail,
)

"""
股票-机构持股
"""
from mssdk.stock_fundamental.stock_hold import (
    stock_institute_hold_detail,
    stock_institute_hold,
)

"""
stock-info
"""
from mssdk.stock.stock_info import (
    stock_info_sh_delist,
    stock_info_sz_delist,
    stock_info_a_code_name,
    stock_info_sh_name_code,
    stock_info_sz_name_code,
    stock_info_sz_change_name,
    stock_info_change_name,
)

"""
stock-sector
"""
from mssdk.stock.stock_industry import stock_sector_spot, stock_sector_detail

"""
stock-fundamental
"""
from mssdk.stock_fundamental.stock_finance import (
    stock_financial_abstract,
    stock_financial_analysis_indicator,
    stock_add_stock,
    stock_ipo_info,
    stock_history_dividend_detail,
    stock_history_dividend,
    stock_circulate_stock_holder,
    stock_restricted_shares,
    stock_fund_stock_holder,
    stock_main_stock_holder,
)

"""
stock_fund
"""
from mssdk.stock.stock_fund import (
    stock_individual_fund_flow,
    stock_market_fund_flow,
    stock_sector_fund_flow_rank,
    stock_individual_fund_flow_rank,
)

"""
air-quality
"""
from mssdk.air.air_zhenqi import (
    air_quality_hist,
    air_quality_rank,
    air_quality_watch_point,
    air_city_list,
)

"""
hf
"""
from mssdk.hf.hf_sp500 import hf_sp_500

"""
stock_em_yjyg
"""
from mssdk.stock_feature.stock_em_yjyg import stock_em_yjyg, stock_em_yysj

"""
stock
"""
from mssdk.stock_feature.stock_em_dxsyl import stock_em_dxsyl, stock_em_xgsglb

"""
article
"""
from mssdk.article.fred_md import fred_md, fred_qd
from mssdk.article.agoyal import agoyal_stock_return

"""
argus
"""
from mssdk.ws.argus import watch_argus

"""
covid_19 CSSE
"""
from mssdk.event.covid import (
    covid_19_csse_daily,
    covid_19_csse_global_confirmed,
    covid_19_csse_global_death,
    covid_19_csse_global_recovered,
    covid_19_csse_us_death,
    covid_19_csse_us_confirmed,
)

"""
futures_cfmmc
"""
from mssdk.futures.futures_cfmmc import futures_index_dict, futures_index_cfmmc

"""
futures_em_spot_stock
"""
from mssdk.futures.futures_em_spot_stock import futures_spot_stock

"""
energy_oil
"""
from mssdk.energy.energy_oil import energy_oil_detail, energy_oil_hist

"""
index-vix
"""
from mssdk.economic.macro_other import index_vix

"""
futures-foreign
"""
from mssdk.futures.futures_foreign import futures_foreign_detail, futures_foreign_hist

"""
stock-em-tfp
"""
from mssdk.stock_feature.stock_em_tfp import stock_em_tfp

"""
stock-em-hsgt
"""
from mssdk.stock_feature.stock_em_hsgt import (
    stock_em_hsgt_north_acc_flow_in,
    stock_em_hsgt_north_cash,
    stock_em_hsgt_north_net_flow_in,
    stock_em_hsgt_south_acc_flow_in,
    stock_em_hsgt_south_cash,
    stock_em_hsgt_south_net_flow_in,
    stock_em_hsgt_hold_stock,
    stock_em_hsgt_hist,
    stock_em_hsgt_institution_statistics,
    stock_em_hsgt_stock_statistics,
    stock_em_hsgt_board_rank,
)

"""
stock-em-comment
"""
from mssdk.stock_feature.stock_em_comment import stock_em_comment

"""
stock-em-analyst
"""
from mssdk.stock_feature.stock_em_analyst import (
    stock_em_analyst_detail,
    stock_em_analyst_rank,
)

"""
tool-github
"""
from mssdk.tool.tool_github import tool_github_star_list, tool_github_email_address

"""
sgx futures data
"""
from mssdk.futures.futures_sgx_daily import futures_sgx_daily

"""
currency interface
"""
from mssdk.currency.currency import (
    currency_convert,
    currency_currencies,
    currency_history,
    currency_latest,
    currency_time_series,
)

"""
知识图谱
"""
from mssdk.nlp.nlp_interface import nlp_ownthink, nlp_answer

"""
微博舆情报告
"""
from mssdk.stock.stock_weibo_nlp import stock_js_weibo_nlp_time, stock_js_weibo_report

"""
金融期权-新浪
"""
from mssdk.option.option_finance_sina import (
    option_sina_cffex_hs300_list,
    option_sina_cffex_hs300_spot,
    option_sina_cffex_hs300_daily,
    option_sina_sse_list,
    option_sina_sse_expire_day,
    option_sina_sse_codes,
    option_sina_sse_spot_price,
    option_sina_sse_underlying_spot_price,
    option_sina_sse_greeks,
    option_sina_sse_minute,
    option_sina_sse_daily,
    option_sina_finance_minute,
)

"""
中国-慈善
"""
from mssdk.charity.charity_china import (
    charity_china_organization,
    charity_china_plan,
    charity_china_platform,
    charity_china_progress,
    charity_china_report,
    charity_china_trust,
)

"""
中国-特许经营数据
"""
from mssdk.event.franchise import franchise_china

"""
债券-沪深债券
"""
from mssdk.bond.zh_bond_sina import bond_zh_hs_daily, bond_zh_hs_spot
from mssdk.bond.zh_bond_cov_sina import (
    bond_zh_hs_cov_daily,
    bond_zh_hs_cov_spot,
    bond_cov_comparison,
    bond_zh_cov,
)
from mssdk.bond.bond_convert import bond_cov_jsl

"""
for pro api
"""
from mssdk.pro.data_pro import pro_api

"""
for pro api token set
"""
from mssdk.utils.token_process import set_token

"""
债券质押式回购成交明细数据
"""
from mssdk.bond.china_repo import bond_repo_zh_tick

"""
新型肺炎
"""
from mssdk.event.covid import (
    covid_19_trip,
    covid_19_history,
)

"""
基金数据接口
"""
from mssdk.fund.fund_em import (
    fund_em_open_fund_daily,
    fund_em_open_fund_info,
    fund_em_etf_fund_daily,
    fund_em_etf_fund_info,
    fund_em_financial_fund_daily,
    fund_em_financial_fund_info,
    fund_em_fund_name,
    fund_em_graded_fund_daily,
    fund_em_graded_fund_info,
    fund_em_money_fund_daily,
    fund_em_money_fund_info,
    fund_em_value_estimation,
)

"""
百度迁徙地图接口
"""
from mssdk.event.covid import (
    migration_area_baidu,
    migration_scale_baidu,
    internal_flow_history,
)

"""
新增-事件接口新型冠状病毒接口
"""
from mssdk.event.covid import (
    covid_19_163,
    covid_19_dxy,
    covid_19_baidu,
    covid_19_hist_city,
    covid_19_hist_province,
)

"""
英为财情-外汇-货币对历史数据
"""
from mssdk.fx.currency_investing import (
    currency_hist,
    currency_name_code,
    currency_pair_map,
)

"""
商品期权-郑州商品交易所-期权-历史数据
"""
from mssdk.option.czce_option import option_czce_hist

"""
宏观-经济数据-银行间拆借利率
"""
from mssdk.interest_rate.interbank_rate_em import rate_interbank

"""
东方财富网-经济数据-银行间拆借利率
"""
from mssdk.interest_rate.interbank_rate_em import rate_interbank

"""
金十数据中心-外汇情绪
"""
from mssdk.economic.macro_other import macro_fx_sentiment

"""
金十数据中心-经济指标-欧元区
"""
from mssdk.economic.macro_euro import (
    macro_euro_gdp_yoy,
    macro_euro_cpi_mom,
    macro_euro_cpi_yoy,
    macro_euro_current_account_mom,
    macro_euro_employment_change_qoq,
    macro_euro_industrial_production_mom,
    macro_euro_manufacturing_pmi,
    macro_euro_ppi_mom,
    macro_euro_retail_sales_mom,
    macro_euro_sentix_investor_confidence,
    macro_euro_services_pmi,
    macro_euro_trade_balance,
    macro_euro_unemployment_rate_mom,
    macro_euro_zew_economic_sentiment,
    macro_euro_lme_holding,
    macro_euro_lme_stock,
)

"""
金十数据中心-经济指标-央行利率-主要央行利率
"""
from mssdk.economic.macro_bank import (
    macro_bank_australia_interest_rate,
    macro_bank_brazil_interest_rate,
    macro_bank_china_interest_rate,
    macro_bank_brazil_interest_rate,
    macro_bank_english_interest_rate,
    macro_bank_euro_interest_rate,
    macro_bank_india_interest_rate,
    macro_bank_japan_interest_rate,
    macro_bank_newzealand_interest_rate,
    macro_bank_russia_interest_rate,
    macro_bank_switzerland_interest_rate,
    macro_bank_usa_interest_rate,
)

"""
交易法门-工具-席位分析
"""
from mssdk.futures_derivative.jyfm_tools_func import (
    jyfm_tools_position_structure,
    jyfm_tools_position_seat_cost,
    jyfm_tools_position_interest_process,
)

"""
交易法门-工具-套利分析
"""
from mssdk.futures_derivative.jyfm_tools_func import (
    jyfm_tools_futures_spread,
    jyfm_tools_futures_ratio,
    jyfm_tools_futures_customize,
    jyfm_exchange_symbol_dict,
    jyfm_tools_futures_full_carry,
    jyfm_tools_futures_arbitrage_matrix,
)

"""
交易法门-工具-资讯汇总
"""
from mssdk.futures_derivative.jyfm_tools_func import (
    jyfm_tools_research_query,
    jyfm_tools_trade_calendar,
)

"""
交易法门-工具-持仓分析
"""
from mssdk.futures_derivative.jyfm_tools_func import (
    jyfm_tools_position_detail,
    jyfm_tools_position_seat,
    jyfm_tools_position_season,
)

"""
交易法门-工具-资金分析
"""
from mssdk.futures_derivative.jyfm_tools_func import (
    jyfm_tools_position_fund_direction,
    jyfm_tools_position_fund_down,
    jyfm_tools_position_fund_season,
    jyfm_tools_position_fund_deal,
)

"""
交易法门-工具-仓单分析
"""
from mssdk.futures_derivative.jyfm_tools_func import (
    jyfm_tools_warehouse_receipt_daily,
    jyfm_tools_warehouse_receipt_query,
    jyfm_tools_warehouse_virtual_fact_ratio,
    jyfm_tools_warehouse_virtual_fact_daily,
)

"""
交易法门-工具-期限分析
"""
from mssdk.futures_derivative.jyfm_tools_func import (
    jyfm_tools_futures_basis_daily,
    jyfm_tools_futures_basis_daily_area,
    jyfm_tools_futures_basis_analysis,
    jyfm_tools_futures_basis_structure,
    jyfm_tools_futures_basis_rule,
)

"""
行情分析
"""
from mssdk.futures_derivative.jyfm_tools_func import jyfm_tools_futures_market

"""
交易法门-工具-交易规则
"""
from mssdk.futures_derivative.jyfm_tools_func import (
    jyfm_tools_receipt_expire_info,
    jyfm_tools_position_limit_info,
    jyfm_tools_symbol_handbook,
)

"""
义乌小商品指数
"""
from mssdk.index.index_yw import index_yw

"""
股票指数-股票指数-成份股
"""
from mssdk.index.index_cons import (
    index_stock_info,
    index_stock_cons,
    index_stock_hist,
    index_stock_cons_sina,
    index_stock_cons_csindex,
    stock_a_code_to_symbol
)

"""
交易法门-工具-数据-黑色系
"""
from mssdk.futures_derivative.jyfm_data_func import (
    jyfm_data_cocking_coal,
    jyfm_data_coke,
)

"""
东方财富-股票账户
"""
from mssdk.stock_feature.stock_em_account import stock_em_account

"""
期货规则
"""
from mssdk.futures.futures_rule import futures_rule

"""
东方财富-商誉专题
"""
from mssdk.stock_feature.stock_em_sy import (
    stock_em_sy_profile,
    stock_em_sy_yq_list,
    stock_em_sy_jz_list,
    stock_em_sy_list,
    stock_em_sy_hy_list,
)

"""
东方财富-股票质押
"""
from mssdk.stock_feature.stock_em_gpzy import (
    stock_em_gpzy_pledge_ratio,
    stock_em_gpzy_profile,
    stock_em_gpzy_distribute_statistics_bank,
    stock_em_gpzy_distribute_statistics_company,
    stock_em_gpzy_industry_data,
    stock_em_gpzy_pledge_ratio_detail,
)

"""
东方财富-机构调研
"""
from mssdk.stock_feature.stock_em_jgdy import stock_em_jgdy_tj, stock_em_jgdy_detail

"""
IT桔子
"""
from mssdk.fortune.it_juzi import death_company, maxima_company, nicorn_company

"""
新浪主力连续接口
"""
from mssdk.futures_derivative.sina_futures_index import (
    futures_main_sina,
    futures_display_main_sina,
)

"""
中国宏观杠杆率数据
"""
from mssdk.economic.marco_cnbs import macro_cnbs

"""
大宗商品-现货价格指数
"""
from mssdk.index.index_spot import spot_goods

"""
成本-世界各大城市生活成本
"""
from mssdk.cost.cost_living import cost_living

"""
能源-碳排放权
"""
from mssdk.energy.energy_carbon import (
    energy_carbon_bj,
    energy_carbon_eu,
    energy_carbon_gz,
    energy_carbon_hb,
    energy_carbon_sz,
)

"""
中国证券投资基金业协会-信息公示
"""
from mssdk.fund.fund_amac import (
    amac_manager_info,
    amac_member_info,
    amac_member_sub_info,
    amac_aoin_info,
    amac_fund_account_info,
    amac_fund_info,
    amac_fund_sub_info,
    amac_futures_info,
    amac_manager_cancelled_info,
    amac_securities_info,
    amac_fund_abs,
    amac_manager_classify_info,
    amac_person_org_list,
)

"""
世界五百强公司排名接口
"""
from mssdk.fortune.fortune_500 import fortune_rank, fortune_rank_eng

"""
申万行业一级
"""
from mssdk.index.index_sw import (
    sw_index_spot,
    sw_index_cons,
    sw_index_daily,
    sw_index_daily_indicator,
)

"""
交易法门-数据-农产品
"""
from mssdk.futures_derivative.jyfm_data_func import (
    jyfm_data_palm,  # 棕榈
    jyfm_data_soybean_meal,  # 豆粕
    jyfm_data_sugar,  # 白糖
    jyfm_data_usa_bean,  # 美豆
    jyfm_data_soybean_oil,  # 豆油
)

"""
交易法门-工具
"""
from mssdk.futures_derivative.jyfm_tools_func import (
    jyfm_tools_futures_customize,  # 棕榈
    jyfm_tools_futures_ratio,  # 豆粕
    jyfm_tools_futures_spread,  # 白糖
    jyfm_tools_receipt_expire_info,  # 美豆
)

"""
交易法门-登录
"""
from mssdk.futures_derivative.jyfm_login_func import jyfm_login

"""
谷歌指数
"""
from mssdk.index.index_google import google_index

"""
百度指数
"""
from mssdk.index.index_baidu import (
    baidu_search_index,
    baidu_info_index,
    baidu_media_index,
)

"""
微博指数
"""
from mssdk.index.index_weibo import weibo_index

"""
经济政策不确定性指数
"""
from mssdk.article.epu_index import article_epu_index

"""
南华期货-南华指数
"""
from mssdk.futures_derivative.nh_index_return import (
    nh_return_index,
    get_nh_list_table,
)
from mssdk.futures_derivative.nh_index_price import nh_price_index
from mssdk.futures_derivative.nh_index_volatility import nh_volatility_index

"""
空气-河北
"""
from mssdk.air.air_hebei import air_quality_hebei

"""
timeanddate-日出和日落
"""
from mssdk.air.time_and_date import sunrise_daily, sunrise_monthly

"""
金十财经-实时监控
"""
from mssdk.ws.js_ws_fx import watch_jinshi_fx
from mssdk.ws.js_ws_quotes import watch_jinshi_quotes

"""
新浪-指数实时行情和历史行情
"""
from mssdk.stock.zh_stock_a_tick_tx_163 import (
    stock_zh_a_tick_tx,
    stock_zh_a_tick_163,
    stock_zh_a_tick_tx_js,
)

"""
新浪-指数实时行情和历史行情
"""
from mssdk.index.zh_stock_index_sina import (
    stock_zh_index_daily,
    stock_zh_index_spot,
    stock_zh_index_daily_tx,
    stock_zh_index_daily_em,
)

"""
外盘期货实时行情
"""
from mssdk.futures.hf_futures_sina import (
    futures_hf_spot,
    hf_subscribe_exchange_symbol,
)

"""
FF多因子数据接口
"""
from mssdk.article.ff_factor import article_ff_crr

"""
Realized Library 接口
"""
from mssdk.article.risk_rv import (
    article_oman_rv,
    article_oman_rv_short,
    article_rlab_rv,
)

"""
银保监分局本级行政处罚数据
"""
from mssdk.bank.bank_cbirc_2020 import bank_fjcf_table_detail

"""
科创板股票
"""
from mssdk.stock.zh_stock_kcb_sina import stock_zh_kcb_spot, stock_zh_kcb_daily

"""
A股
"""
from mssdk.stock.zh_stock_a_sina import (
    stock_zh_a_spot,
    stock_zh_a_daily,
    stock_zh_a_minute,
    stock_zh_a_cdr_daily,
)

"""
A+H股
"""
from mssdk.stock.zh_stock_ah_tx import (
    stock_zh_ah_spot,
    stock_zh_ah_daily,
    stock_zh_ah_name,
)

"""
加密货币
"""
from mssdk.economic.macro_other import crypto_js_spot

"""
金融期权
"""
from mssdk.option.option_finance import (
    option_finance_board,
    option_finance_underlying,
)

"""
新浪-美股实时行情数据和历史行情数据(前复权)
"""
from mssdk.stock.us_stock_sina import (
    stock_us_daily,
    stock_us_spot,
    get_us_stock_name,
    stock_us_fundamental,
)

"""
新浪-港股实时行情数据和历史数据(前复权和后复权因子)
"""
from mssdk.stock.hk_stock_sina import stock_hk_daily, stock_hk_spot

"""
新浪-期货实时数据
"""
from mssdk.futures.futures_zh_sina import futures_zh_spot, match_main_contract

"""
西本新干线-指数数据
"""
from mssdk.futures_derivative.futures_xgx import _get_code_pic, futures_xgx_index

"""
生意社-商品与期货-现期图数据
"""
from mssdk.futures_derivative.sys_spot_futures import (
    get_sys_spot_futures,
    get_sys_spot_futures_dict,
)

"""
交易法门-套利工具-跨期价差(自由价差)
"""
from mssdk.futures_derivative.jyfm_tools_func import (
    jyfm_tools_futures_ratio,
    jyfm_tools_futures_customize,
    jyfm_tools_futures_spread,
)

"""
和讯财经-行情及历史数据
"""
from mssdk.stock.us_zh_stock_hx import stock_us_zh_spot, stock_us_zh_daily

"""
和讯财经-企业社会责任
"""
from mssdk.stock.zh_stock_zrbg_hx import stock_zh_a_scr_report

"""
期货-仓单有效期
"""
from mssdk.futures.receipt_period import get_receipt_date

"""
全球宏观-机构宏观
"""
from mssdk.economic.macro_constitute import (
    macro_cons_gold_amount,
    macro_cons_gold_change,
    macro_cons_gold_volume,
    macro_cons_opec_month,
    macro_cons_silver_amount,
    macro_cons_silver_change,
    macro_cons_silver_volume,
)

"""
全球宏观-美国宏观
"""
from mssdk.economic.macro_usa import (
    macro_usa_eia_crude_rate,
    macro_usa_non_farm,
    macro_usa_unemployment_rate,
    macro_usa_adp_employment,
    macro_usa_core_pce_price,
    macro_usa_cpi_monthly,
    macro_usa_crude_inner,
    macro_usa_gdp_monthly,
    macro_usa_initial_jobless,
    macro_usa_lmci,
    macro_usa_api_crude_stock,
    macro_usa_building_permits,
    macro_usa_business_inventories,
    macro_usa_cb_consumer_confidence,
    macro_usa_core_cpi_monthly,
    macro_usa_core_ppi,
    macro_usa_current_account,
    macro_usa_durable_goods_orders,
    macro_usa_trade_balance,
    macro_usa_spcs20,
    macro_usa_services_pmi,
    macro_usa_rig_count,
    macro_usa_retail_sales,
    macro_usa_real_consumer_spending,
    macro_usa_ppi,
    macro_usa_pmi,
    macro_usa_personal_spending,
    macro_usa_pending_home_sales,
    macro_usa_nfib_small_business,
    macro_usa_new_home_sales,
    macro_usa_nahb_house_market_index,
    macro_usa_michigan_consumer_sentiment,
    macro_usa_exist_home_sales,
    macro_usa_export_price,
    macro_usa_factory_orders,
    macro_usa_house_price_index,
    macro_usa_house_starts,
    macro_usa_import_price,
    macro_usa_industrial_production,
    macro_usa_ism_non_pmi,
    macro_usa_ism_pmi,
    macro_usa_job_cuts,
    macro_usa_cftc_nc_holding,
    macro_usa_cftc_c_holding,
    macro_usa_cftc_merchant_currency_holding,
    macro_usa_cftc_merchant_goods_holding,
)

"""
全球宏观-中国宏观
"""
from mssdk.economic.macro_china import (
    macro_china_cpi_monthly,
    macro_china_cpi_yearly,
    macro_china_m2_yearly,
    macro_china_fx_reserves_yearly,
    macro_china_cx_pmi_yearly,
    macro_china_pmi_yearly,
    macro_china_daily_energy,
    macro_china_non_man_pmi,
    macro_china_rmb,
    macro_china_gdp_yearly,
    macro_china_ppi_yearly,
    macro_china_cx_services_pmi_yearly,
    macro_china_market_margin_sh,
    macro_china_market_margin_sz,
    macro_china_au_report,
    macro_china_ctci_detail,
    macro_china_ctci_detail_hist,
    macro_china_ctci,
    macro_china_exports_yoy,
    macro_china_hk_market_info,
    macro_china_imports_yoy,
    macro_china_trade_balance,
    macro_china_shibor_all,
    macro_china_industrial_production_yoy,
    macro_china_lpr,
    macro_china_new_house_price,
    macro_china_enterprise_boom_index,
    macro_china_national_tax_receipts,
    macro_china_new_financial_credit,
    macro_china_fx_gold,
    macro_china_money_supply,
    macro_china_stock_market_cap,
    macro_china_cpi,
    macro_china_gdp,
    macro_china_ppi,
    macro_china_pmi,
    macro_china_gdzctz,
    macro_china_hgjck,
    macro_china_czsr,
    macro_china_whxd,
    macro_china_wbck,
    macro_china_bond_public,
    macro_china_gksccz,
    macro_china_hb,
    macro_china_xfzxx,
    macro_china_reserve_requirement_ratio,
    macro_china_consumer_goods_retail,
    macro_china_society_electricity,
    macro_china_society_traffic_volume,
    macro_china_postal_telecommunicational,
    macro_china_international_tourism_fx,
    macro_china_passenger_load_factor,
    macro_china_freight_index,
    macro_china_central_bank_balance,
    macro_china_insurance,
    macro_china_supply_of_money,
    macro_china_swap_rate,
    macro_china_foreign_exchange_gold,
    macro_china_retail_price_index,
    macro_china_real_estate,
)

"""
全球期货
"""
from mssdk.futures.international_futures import (
    get_sector_futures,
    futures_global_commodity_name_url_map,
)

"""
外汇
"""
from mssdk.fx.fx_quote import fx_pair_quote, fx_spot_quote, fx_swap_quote

"""
债券行情
"""
from mssdk.bond.china_bond import bond_spot_quote, bond_spot_deal, bond_china_yield

"""
商品期权
"""
from mssdk.option.option_commodity import (
    get_dce_option_daily,
    get_czce_option_daily,
    get_shfe_option_daily,
)

"""
英为财情-债券
"""
from mssdk.bond.bond_investing import (
    bond_investing_global,
    bond_investing_global_country_name_url,
)

"""
英为财情-指数
"""
from mssdk.index.index_investing import (
    index_investing_global,
    index_investing_global_country_name_url,
)

"""
99期货-期货库存数据
"""
from mssdk.futures.futures_inventory import futures_inventory_99

"""
东方财富-期货库存数据
"""
from mssdk.futures.futures_inventory_em import futures_inventory_em

"""
中国银行间市场交易商协会
"""
from mssdk.bond.bond_bank import get_bond_bank

"""
奇货可查-工具模块
"""
from mssdk.qhkc_web.qhkc_tool import qhkc_tool_foreign, qhkc_tool_gdp

"""
奇货可查-指数模块
"""
from mssdk.qhkc_web.qhkc_index import (
    get_qhkc_index,
    get_qhkc_index_trend,
    get_qhkc_index_profit_loss,
)

"""
奇货可查-资金模块
"""
from mssdk.qhkc_web.qhkc_fund import (
    get_qhkc_fund_money_change,
    get_qhkc_fund_bs,
    get_qhkc_fund_position,
)

"""
大宗商品现货价格及基差
"""
from mssdk.futures.futures_basis import futures_spot_price_daily, futures_spot_price, futures_spot_price_previous

"""
期货持仓成交排名数据
"""
from mssdk.futures.cot import (
    get_rank_sum_daily,
    get_rank_sum,
    get_shfe_rank_table,
    get_czce_rank_table,
    get_dce_rank_table,
    get_cffex_rank_table,
    futures_dce_position_rank,
    futures_dce_position_rank_other,
)

"""
大宗商品仓单数据
"""
from mssdk.futures.receipt import get_receipt

"""
大宗商品展期收益率数据
"""
from mssdk.futures.futures_roll_yield import get_roll_yield_bar, get_roll_yield

"""
交易所日线行情数据
"""
from mssdk.futures.futures_daily_bar import (
    get_cffex_daily,
    get_czce_daily,
    get_shfe_v_wap,
    get_shfe_daily,
    get_dce_daily,
    get_futures_daily,
)
