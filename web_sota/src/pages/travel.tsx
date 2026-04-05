import { Card, CardHeader, CardTitle, CardDescription, CardContent } from '@/components/ui/card';
import { TrainFront, Map, Calendar, Plane } from 'lucide-react';

export function Travel() {
    return (
        <div className="space-y-6">
            <div className="flex flex-col gap-2">
                <h1 className="text-3xl font-black tracking-tight text-white">Travel Planner</h1>
                <p className="text-slate-400 font-medium">Coordinate your Viennese transit and international voyages.</p>
            </div>

            <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
                <Card className="bg-slate-900/50 border-slate-800 backdrop-blur-sm">
                    <CardHeader>
                        <CardTitle className="flex items-center gap-2">
                            <TrainFront className="h-5 w-5 text-purple-400" />
                            ÖBB / Wiener Linien
                        </CardTitle>
                        <CardDescription>Real-time transit monitoring</CardDescription>
                    </CardHeader>
                    <CardContent>
                        <p className="text-sm text-slate-400">Next departures from Alser Straße and Westbahnhof.</p>
                    </CardContent>
                </Card>

                <Card className="bg-slate-900/50 border-slate-800 backdrop-blur-sm">
                    <CardHeader>
                        <CardTitle className="flex items-center gap-2">
                            <Plane className="h-5 w-5 text-indigo-400" />
                            Flight Status
                        </CardTitle>
                        <CardDescription>Vienna International (VIE)</CardDescription>
                    </CardHeader>
                    <CardContent>
                        <p className="text-sm text-slate-400">Track arrivals and departures for your next trip.</p>
                    </CardContent>
                </Card>

                <Card className="bg-slate-900/50 border-slate-800 backdrop-blur-sm">
                    <CardHeader>
                        <CardTitle className="flex items-center gap-2">
                            <Map className="h-5 w-5 text-blue-400" />
                            Destinations
                        </CardTitle>
                        <CardDescription>Japan & China Logistics</CardDescription>
                    </CardHeader>
                    <CardContent>
                        <p className="text-sm text-slate-400">Monthly/Yearly residency patterns and efficiency logs.</p>
                    </CardContent>
                </Card>
            </div>
        </div>
    );
}
