---
{
  "projection_kind": "taulib_declaration",
  "title": "K3_orbit_seeded",
  "permalink": "/verify/taulib/docs/book-i-kernel-axioms/k3-orbit-seeded/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Kernel.Axioms`.",
  "declaration_id": "TauLib.BookI.Kernel.Axioms::K3_orbit_seeded",
  "declaration_slug": "k3-orbit-seeded",
  "kind": "theorem",
  "name": "K3_orbit_seeded",
  "module_name": "TauLib.BookI.Kernel.Axioms",
  "module_url": "/verify/taulib/docs/book-i-kernel-axioms/",
  "source_line_start": 97,
  "source_line_end": 99,
  "registry_ids": [
    "I.K3"
  ],
  "related_registry_items": [
    {
      "id": "I.K3",
      "title": "Orbit-Seeded Generation (K3)",
      "url": "/registry/object/I.K3/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Axioms.lean#L97-L99",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Kernel.Axioms",
        "url": "/verify/taulib/docs/book-i-kernel-axioms/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Axioms.lean#L97-L99",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookI.Kernel.Axioms](/verify/taulib/docs/book-i-kernel-axioms/)
- Source path: [`TauLib/BookI/Kernel/Axioms.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Kernel/Axioms.lean#L97-L99)
- Source range: L97-L99
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.K3` — Orbit-Seeded Generation (K3)

## Immediate Comment / Docstring

```lean
/-- [I.K3] Every non-omega generator seeds an orbit ray containing itself. -/
```

## Source Excerpt

```lean
theorem K3_orbit_seeded (g : Generator) (h : g ≠ omega) :
    inOrbitRay g (TauObj.ofGen g) := by
  exact ⟨rfl, h⟩
```
