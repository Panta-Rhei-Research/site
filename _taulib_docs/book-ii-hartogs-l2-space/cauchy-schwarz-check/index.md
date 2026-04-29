---
{
  "projection_kind": "taulib_declaration",
  "title": "cauchy_schwarz_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-l2-space/cauchy-schwarz-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.L2Space`.",
  "declaration_id": "TauLib.BookII.Hartogs.L2Space::cauchy_schwarz_check",
  "declaration_slug": "cauchy-schwarz-check",
  "kind": "def",
  "name": "cauchy_schwarz_check",
  "module_name": "TauLib.BookII.Hartogs.L2Space",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-l2-space/",
  "source_line_start": 107,
  "source_line_end": 111,
  "registry_ids": [
    "II.T53"
  ],
  "related_registry_items": [
    {
      "id": "II.T53",
      "title": "Cauchy-Schwarz Inequality",
      "url": "/registry/object/II.T53/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/L2Space.lean#L107-L111",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.L2Space",
        "url": "/verify/taulib/docs/book-ii-hartogs-l2-space/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/L2Space.lean#L107-L111",
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

- Module: [TauLib.BookII.Hartogs.L2Space](/verify/taulib/docs/book-ii-hartogs-l2-space/)
- Source path: [`TauLib/BookII/Hartogs/L2Space.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/L2Space.lean#L107-L111)
- Source range: L107-L111
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.T53` — Cauchy-Schwarz Inequality

## Immediate Comment / Docstring

```lean
/-- [II.T53] Cauchy-Schwarz check: |⟨f,g⟩|² ≤ ‖f‖² · ‖g‖².
    As integers: (Σ fg)² ≤ (Σ f²)(Σ g²). -/
```

## Source Excerpt

```lean
def cauchy_schwarz_check (f g : Nat → Int) (k : Nat) : Bool :=
  let ip := inner_product_sum f g k
  let nf := l2_norm_sq f k
  let ng := l2_norm_sq g k
  ip * ip ≤ nf * ng
```
