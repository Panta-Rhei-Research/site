---
{
  "projection_kind": "taulib_declaration",
  "title": "nesting_check",
  "permalink": "/verify/taulib/docs/book-ii-domains-cylinders/nesting-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Domains.Cylinders`.",
  "declaration_id": "TauLib.BookII.Domains.Cylinders::nesting_check",
  "declaration_slug": "nesting-check",
  "kind": "def",
  "name": "nesting_check",
  "module_name": "TauLib.BookII.Domains.Cylinders",
  "module_url": "/verify/taulib/docs/book-ii-domains-cylinders/",
  "source_line_start": 88,
  "source_line_end": 96,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/Cylinders.lean#L88-L96",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Domains.Cylinders",
        "url": "/verify/taulib/docs/book-ii-domains-cylinders/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/Cylinders.lean#L88-L96",
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

- Module: [TauLib.BookII.Domains.Cylinders](/verify/taulib/docs/book-ii-domains-cylinders/)
- Source path: [`TauLib/BookII/Domains/Cylinders.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Domains/Cylinders.lean#L88-L96)
- Source range: L88-L96
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [II.T04, clause 1] Nesting: C_{k+1}(x) ⊆ C_k(x).
    If y ≡ x mod M_{k+1} then y ≡ x mod M_k (since M_k | M_{k+1}). -/
```

## Source Excerpt

```lean
def nesting_check (x k bound : TauIdx) : Bool :=
  go 2 (bound + 1)
where
  go (y fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if y > bound then true
    else (!cylinder_mem (k + 1) x y || cylinder_mem k x y) &&
         go (y + 1) (fuel - 1)
  termination_by fuel
```
