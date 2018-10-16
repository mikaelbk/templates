public class Particle{
    public Particle(double mass, double[] r){
        this.mass = mass;
        this.r = r;
        this.v = new double[r.length];
        this.a = new double[r.length];
    }

    double mass;
    double[] r;
    double[] v;
    double[] a;

    public double[] getPosition(){
        return r;
    }

    public void moveParticle(double[] force, double dt){
        for(int i = 0; i < force.length; i++){
            a[i] = force[i]/mass;
            v[i] += a[i]*dt;
            r[i] += v[i]*dt;
        }
    }
}