import { Card, CardHeader, CardTitle, CardDescription, CardContent } from '@/components/ui/card';
import { Calendar, CheckSquare, Target, Zap } from 'lucide-react';

export function Planning() {
    return (
        <div className="space-y-6">
            <div className="flex flex-col gap-2">
                <h1 className="text-3xl font-black tracking-tight text-white">Efficiency Planner</h1>
                <p className="text-slate-400 font-medium">High-bandwidth life orchestration and goal tracking.</p>
            </div>

            <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
                <Card className="bg-slate-900/50 border-slate-800 backdrop-blur-sm">
                    <CardHeader>
                        <CardTitle className="flex items-center gap-2">
                            <Target className="h-5 w-5 text-red-400" />
                            Milestones
                        </CardTitle>
                        <CardDescription>Annual objectives</CardDescription>
                    </CardHeader>
                    <CardContent>
                        <p className="text-sm text-slate-400">Tracking progress on major personal and technical goals.</p>
                    </CardContent>
                </Card>
            </div>
        </div>
    );
}
