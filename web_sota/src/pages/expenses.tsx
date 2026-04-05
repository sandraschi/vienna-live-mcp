import { Card, CardHeader, CardTitle, CardDescription, CardContent } from '@/components/ui/card';
import { Wallet, Receipt, PieChart, Landmark } from 'lucide-react';

export function Expenses() {
    return (
        <div className="space-y-6">
            <div className="flex flex-col gap-2">
                <h1 className="text-3xl font-black tracking-tight text-white">Expense Tracker</h1>
                <p className="text-slate-400 font-medium">Reductionist financial auditing and asset management.</p>
            </div>

            <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
                <Card className="bg-slate-900/50 border-slate-800 backdrop-blur-sm">
                    <CardHeader>
                        <CardTitle className="flex items-center gap-2">
                            <Wallet className="h-5 w-5 text-emerald-400" />
                            Liquidity
                        </CardTitle>
                        <CardDescription>Real-time cashflow</CardDescription>
                    </CardHeader>
                    <CardContent>
                        <p className="text-sm text-slate-400">Monitoring Viennese cost-of-living and efficiency.</p>
                    </CardContent>
                </Card>
            </div>
        </div>
    );
}
