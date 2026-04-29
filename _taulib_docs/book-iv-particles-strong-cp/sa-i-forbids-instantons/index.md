---
{
  "projection_kind": "taulib_declaration",
  "title": "sa_i_forbids_instantons",
  "permalink": "/verify/taulib/docs/book-iv-particles-strong-cp/sa-i-forbids-instantons/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Particles.StrongCP`.",
  "declaration_id": "TauLib.BookIV.Particles.StrongCP::sa_i_forbids_instantons",
  "declaration_slug": "sa-i-forbids-instantons",
  "kind": "theorem",
  "name": "sa_i_forbids_instantons",
  "module_name": "TauLib.BookIV.Particles.StrongCP",
  "module_url": "/verify/taulib/docs/book-iv-particles-strong-cp/",
  "source_line_start": 57,
  "source_line_end": 58,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/StrongCP.lean#L57-L58",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/StrongCP.lean#L57-L58",
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

- Module: [TauLib.BookIV.Particles.StrongCP](/verify/taulib/docs/book-iv-particles-strong-cp/)
- Source path: [`TauLib/BookIV/Particles/StrongCP.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Particles/StrongCP.lean#L57-L58)
- Source range: L57-L58
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Instanton winding increment = 1, which is not ≡ 0 mod 3.
    Anti-instanton winding increment = −1 ≡ 2, which is also not ≡ 0 mod 3.
    SA-i allows only Δ ≡ 0 mod 3, so both are forbidden. -/
```

## Source Excerpt

```lean
theorem sa_i_forbids_instantons :
    (1 : Int) % 3 ≠ 0 ∧ (-1 : Int) % 3 ≠ 0 := by decide
```
