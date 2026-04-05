import { Activity, Cpu, HardDrive, Database } from 'lucide-react';
import { useEffect, useState } from 'react';

interface Stats {
    status: string;
    system: {
        cpu_percent: number;
        memory: { percent: number };
        disk: { percent: number };
    };
}

export function Status() {
    const [stats, setStats] = useState<Stats | null>(null);

    useEffect(() => {
        const fetchStatus = async () => {
            try {
                // Fetching from the get_server_status tool endpoint
                // Note: Standard FastMCP tools are under /mcp/tools or specialized endpoints
                // For simplicity in this SOTA template, we assume a /health or similar metrics endpoint
                const res = await fetch('http://localhost:10879/health');
                const data = await res.json();
                setStats(data);
            } catch (err) {
                console.error('Failed to fetch stats', err);
            }
        };
        fetchStatus();
        const interval = setInterval(fetchStatus, 5000);
        return () => clearInterval(interval);
    }, []);

    return (
        <div className="space-y-6">
            <header>
                <h2 className="text-3xl font-bold tracking-tight text-slate-100">System Status</h2>
                <p className="text-slate-400">Real-time health and performance metrics for Vienna Live MCP.</p>
            </header>

            <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
                <div className="rounded-xl border border-slate-800 bg-slate-900/50 p-6 backdrop-blur-sm">
                    <div className="flex items-center gap-4">
                        <Activity className="h-8 w-8 text-emerald-500" />
                        <div>
                            <p className="text-sm font-medium text-slate-400">Server Status</p>
                            <p className="text-2xl font-bold text-slate-100 uppercase">{stats?.status || 'Online'}</p>
                        </div>
                    </div>
                </div>

                <div className="rounded-xl border border-slate-800 bg-slate-900/50 p-6 backdrop-blur-sm">
                    <div className="flex items-center gap-4">
                        <Cpu className="h-8 w-8 text-blue-500" />
                        <div>
                            <p className="text-sm font-medium text-slate-400">CPU Usage</p>
                            <p className="text-2xl font-bold text-slate-100">{stats?.system.cpu_percent || 0}%</p>
                        </div>
                    </div>
                </div>

                <div className="rounded-xl border border-slate-800 bg-slate-900/50 p-6 backdrop-blur-sm">
                    <div className="flex items-center gap-4">
                        <Database className="h-8 w-8 text-purple-500" />
                        <div>
                            <p className="text-sm font-medium text-slate-400">Memory Load</p>
                            <p className="text-2xl font-bold text-slate-100">{stats?.system.memory.percent || 0}%</p>
                        </div>
                    </div>
                </div>

                <div className="rounded-xl border border-slate-800 bg-slate-900/50 p-6 backdrop-blur-sm">
                    <div className="flex items-center gap-4">
                        <HardDrive className="h-8 w-8 text-amber-500" />
                        <div>
                            <p className="text-sm font-medium text-slate-400">Disk Usage</p>
                            <p className="text-2xl font-bold text-slate-100">{stats?.system.disk.percent || 0}%</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
