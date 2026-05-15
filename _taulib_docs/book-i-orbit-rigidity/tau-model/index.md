---
{
  "projection_kind": "taulib_declaration",
  "title": "TauModel",
  "permalink": "/corpus/taulib/docs/book-i-orbit-rigidity/tau-model/",
  "summary_short": "`structure` declaration in `TauLib.BookI.Orbit.Rigidity`.",
  "declaration_id": "TauLib.BookI.Orbit.Rigidity::TauModel",
  "declaration_slug": "tau-model",
  "kind": "structure",
  "name": "TauModel",
  "module_name": "TauLib.BookI.Orbit.Rigidity",
  "module_url": "/corpus/taulib/docs/book-i-orbit-rigidity/",
  "source_line_start": 141,
  "source_line_end": 146,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Rigidity.lean#L141-L146",
  "formal_status": "defined",
  "declaration_role": "type/data schema",
  "formal_status_label": "type/data schema",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.Rigidity",
        "url": "/corpus/taulib/docs/book-i-orbit-rigidity/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Rigidity.lean#L141-L146",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "role": "type/data schema",
      "status": "type/data schema"
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

- Module: [TauLib.BookI.Orbit.Rigidity](/corpus/taulib/docs/book-i-orbit-rigidity/)
- Source path: [`TauLib/BookI/Orbit/Rigidity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Rigidity.lean#L141-L146)
- Source range: L141-L146
- Kind: `structure`
- Public role: `type/data schema`
- Formal status hint: `type/data schema`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- A model of the τ₀ axioms. -/
```

## Source Excerpt

```lean
structure TauModel where
  Carrier : Type
  gen : Generator → Carrier
  rho_model : Carrier → Carrier
  gen_distinct_ax : ∀ g h : Generator, g ≠ h → gen g ≠ gen h
  omega_fixed_ax : rho_model (gen omega) = gen omega
```
