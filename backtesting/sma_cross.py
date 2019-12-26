from datetime import datetime

import backtrader as bt
import click


class SmaCross(bt.SignalStrategy):
    def __init__(self):
        sma1, sma2 = bt.ind.SMA(period=5), bt.ind.SMA(period=10)

        crossover = bt.ind.CrossOver(sma1, sma2)
        self.signal_add(bt.SIGNAL_LONG, crossover)


@click.command()
@click.option('--cash', default=5000)
@click.option('--stock', default='AAPL')
def main(cash, stock):
    cerebro = bt.Cerebro()
    cerebro.broker.set_cash(cash)
    cerebro.addsizer(bt.sizers.AllInSizer)
    cerebro.addstrategy(SmaCross)
    cerebro.addwriter(bt.WriterFile, out='{}.csv'.format(stock), csv=True)

    data = bt.feeds.YahooFinanceData(dataname=stock,
                                     fromdate=datetime(2009, 12, 24),
                                     todate=datetime(2019, 12, 24))
    cerebro.adddata(data)

    cerebro.run()
    cerebro.plot()


if __name__ == '__main__':
    main()
