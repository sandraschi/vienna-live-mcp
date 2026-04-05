import { Card, CardHeader, CardTitle, CardDescription, CardContent } from '@/components/ui/card';
import { Music } from 'lucide-react';

export function Media() {
    return (
        <div className="space-y-6">
            <div className="flex flex-col gap-2">
                <h1 className="text-3xl font-black tracking-tight text-white">Media Nexus</h1>
                <p className="text-slate-400 font-medium">Orchestrating Plex, VirtualDJ, and personal collections.</p>
            </div>

            <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
                <Card className="bg-slate-900/50 border-slate-800 backdrop-blur-sm">
                    <CardHeader>
                        <CardTitle className="flex items-center gap-2">
                            <Music className="h-5 w-5 text-indigo-400" />
                            Library
                        </CardTitle>
                        <CardDescription>Viennese Archive</CardDescription>
                    </CardHeader>
                    <CardContent>
                        <p className="text-sm text-slate-400">Lossless audio and high-fidelity media management.</p>
                    </CardContent>
                </Card>
            </div>
        </div>
    );
}
