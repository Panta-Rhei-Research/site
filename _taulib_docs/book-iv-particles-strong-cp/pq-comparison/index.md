---
{
  "projection_kind": "taulib_declaration",
  "title": "pq_comparison",
  "permalink": "/verify/taulib/docs/book-iv-particles-strong-cp/pq-comparison/",
  "summary_short": "`def` declaration in `TauLib.BookIV.Particles.StrongCP`.",
  "declaration_id": "TauLib.BookIV.Particles.StrongCP::pq_comparison",
  "declaration_slug": "pq-comparison",
  "kind": "def",
  "name": "pq_comparison",
  "module_name": "TauLib.BookIV.Particles.StrongCP",
  "module_url": "/verify/taulib/docs/book-iv-particles-strong-cp/",
  "source_line_start": 116,
  "source_line_end": 121,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/StrongCP.lean#L116-L121",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Particles.StrongCP",
        "url": "/verify/taulib/docs/book-iv-particles-strong-cp/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/StrongCP.lean#L116-L121",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookIV.Particles.StrongCP](/verify/taulib/docs/book-iv-particles-strong-cp/)
- Source path: [`TauLib/BookIV/Particles/StrongCP.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/StrongCP.lean#L116-L121)
- Source range: L116-L121
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Comparison of strong CP resolutions:
    PQ:       U(1)_PQ → pseudo-Goldstone axion (new field, m_a ~ 10⁻⁵ eV,
              f_PQ free parameter ~ 10¹² GeV)
    Nelson-Barr: CP mediators (new fields, mediator scale free)
    τ/SA-i:   No new fields; θ_QCD = 0 from K3 + K5 τ-axioms alone.
    The SA-i resolution is the most parsimonious: zero new entities, zero
    new parameters, structural derivation from the existing τ-axiom set.
    Scope: tau-effective. -/
```

## Source Excerpt

```lean
def pq_comparison : String :=
  "SA-i resolves strong CP from axioms K3+K5: no axion, no new symmetry, " ++
  "no free parameter. Comparison: PQ (new U(1) + axion), Nelson-Barr (new mediators), " ++
  "SA-i (mod-3 winding constraint from existing axioms)."

end Tau.BookIV.Particles
```
