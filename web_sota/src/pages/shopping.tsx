import { Card, CardHeader, CardTitle, CardDescription, CardContent } from '@/components/ui/card';
import { ShoppingBag, Tag, Calculator, TrendingUp } from 'lucide-react';

export function Shopping() {
    return (
        <div className="space-y-6">
            <div className="flex flex-col gap-2">
                <h1 className="text-3xl font-black tracking-tight text-white">Shopping Manager</h1>
                <p className="text-slate-400 font-medium">Billa Plus, Hofer, and Spar optimization engine.</p>
            </div>

            <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
                <Card className="bg-slate-900/50 border-slate-800 backdrop-blur-sm">
                    <CardHeader>
                        <CardTitle className="flex items-center gap-2">
                            <ShoppingBag className="h-5 w-5 text-indigo-400" />
                            Inventory
                        </CardTitle>
                        <CardDescription>Current household stock</CardDescription>
                    </CardHeader>
                    <CardContent>
                        <p className="text-sm text-slate-400">Real-time tracking of Viennese household supplies.</p>
                    </CardContent>
                </Card>

                <Card className="bg-slate-900/50 border-slate-800 backdrop-blur-sm">
                    <CardHeader>
                        <CardTitle className="flex items-center gap-2">
                            <Tag className="h-5 w-5 text-pink-400" />
                            Offer Analysis
                        </CardTitle>
                        <CardDescription>Price reduction tracking</CardDescription>
                    </CardHeader>
                    <CardContent>
                        <p className="text-sm text-slate-400">Automated discount detection for Spar and Billa.</p>
                    </CardContent>
                </Card>
            </div>
        </div>
    );
}
