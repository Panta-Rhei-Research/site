---
{
  "projection_kind": "taulib_declaration",
  "title": "primorial_ratio_check",
  "permalink": "/verify/taulib/docs/book-ii-transcendentals-eearned/primorial-ratio-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Transcendentals.EEarned`.",
  "declaration_id": "TauLib.BookII.Transcendentals.EEarned::primorial_ratio_check",
  "declaration_slug": "primorial-ratio-check",
  "kind": "def",
  "name": "primorial_ratio_check",
  "module_name": "TauLib.BookII.Transcendentals.EEarned",
  "module_url": "/verify/taulib/docs/book-ii-transcendentals-eearned/",
  "source_line_start": 102,
  "source_line_end": 114,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/EEarned.lean#L102-L114",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Transcendentals.EEarned",
        "url": "/verify/taulib/docs/book-ii-transcendentals-eearned/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/EEarned.lean#L102-L114",
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

- Module: [TauLib.BookII.Transcendentals.EEarned](/verify/taulib/docs/book-ii-transcendentals-eearned/)
- Source path: [`TauLib/BookII/Transcendentals/EEarned.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/EEarned.lean#L102-L114)
- Source range: L102-L114
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Primorial ratios match primes: P_{k+1}/P_k = p_{k+1} exactly. -/
```

## Source Excerpt

```lean
def primorial_ratio_check (stages : TauIdx) : Bool :=
  go 1 (stages + 1)
where
  go (k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k > stages then true
    else
      let pk := primorial k
      let pk1 := primorial (k + 1)
      let next_p := nth_prime (k + 1)
      (pk > 0 && pk1 / pk == next_p && pk1 % pk == 0) &&
      go (k + 1) (fuel - 1)
  termination_by fuel
```
