---
{
  "projection_kind": "taulib_declaration",
  "title": "interpret",
  "permalink": "/corpus/taulib/docs/book-i-orbit-rigidity/interpret/",
  "summary_short": "`def` declaration in `TauLib.BookI.Orbit.Rigidity`.",
  "declaration_id": "TauLib.BookI.Orbit.Rigidity::interpret",
  "declaration_slug": "interpret",
  "kind": "def",
  "name": "interpret",
  "module_name": "TauLib.BookI.Orbit.Rigidity",
  "module_url": "/corpus/taulib/docs/book-i-orbit-rigidity/",
  "source_line_start": 149,
  "source_line_end": 150,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Rigidity.lean#L149-L150",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Rigidity.lean#L149-L150",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "definition",
      "status": "definition"
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
- Source path: [`TauLib/BookI/Orbit/Rigidity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Orbit/Rigidity.lean#L149-L150)
- Source range: L149-L150
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The canonical map: ⟨g, n⟩ ↦ ρ_M^n(g_M). -/
```

## Source Excerpt

```lean
def interpret (M : TauModel) (x : TauObj) : M.Carrier :=
  Nat.rec (M.gen x.seed) (fun _ ih => M.rho_model ih) x.depth
```
