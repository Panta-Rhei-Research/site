---
{
  "projection_kind": "taulib_declaration",
  "title": "OrbitRay",
  "permalink": "/verify/taulib/docs/book-i-orbit-generation/orbit-ray/",
  "summary_short": "`def` declaration in `TauLib.BookI.Orbit.Generation`.",
  "declaration_id": "TauLib.BookI.Orbit.Generation::OrbitRay",
  "declaration_slug": "orbit-ray",
  "kind": "def",
  "name": "OrbitRay",
  "module_name": "TauLib.BookI.Orbit.Generation",
  "module_url": "/verify/taulib/docs/book-i-orbit-generation/",
  "source_line_start": 83,
  "source_line_end": 84,
  "registry_ids": [
    "I.D05"
  ],
  "related_registry_items": [
    {
      "id": "I.D05",
      "title": "Orbit Rays",
      "url": "/registry/object/I.D05/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Generation.lean#L83-L84",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Orbit.Generation",
        "url": "/verify/taulib/docs/book-i-orbit-generation/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Generation.lean#L83-L84",
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

- Module: [TauLib.BookI.Orbit.Generation](/verify/taulib/docs/book-i-orbit-generation/)
- Source path: [`TauLib/BookI/Orbit/Generation.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Generation.lean#L83-L84)
- Source range: L83-L84
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D05` — Orbit Rays

## Immediate Comment / Docstring

```lean
/-- [I.D05] Orbit ray membership predicate: x ∈ O_g iff x has seed g
    and g is not omega. -/
```

## Source Excerpt

```lean
def OrbitRay (g : Generator) (x : TauObj) : Prop :=
  x.seed = g ∧ g ≠ omega
```
