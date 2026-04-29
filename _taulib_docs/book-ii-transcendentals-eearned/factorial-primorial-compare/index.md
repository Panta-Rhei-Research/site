---
{
  "projection_kind": "taulib_declaration",
  "title": "factorial_primorial_compare",
  "permalink": "/verify/taulib/docs/book-ii-transcendentals-eearned/factorial-primorial-compare/",
  "summary_short": "`def` declaration in `TauLib.BookII.Transcendentals.EEarned`.",
  "declaration_id": "TauLib.BookII.Transcendentals.EEarned::factorial_primorial_compare",
  "declaration_slug": "factorial-primorial-compare",
  "kind": "def",
  "name": "factorial_primorial_compare",
  "module_name": "TauLib.BookII.Transcendentals.EEarned",
  "module_url": "/verify/taulib/docs/book-ii-transcendentals-eearned/",
  "source_line_start": 128,
  "source_line_end": 129,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/EEarned.lean#L128-L129",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/EEarned.lean#L128-L129",
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
- Source path: [`TauLib/BookII/Transcendentals/EEarned.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Transcendentals/EEarned.lean#L128-L129)
- Source range: L128-L129
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Factorial vs primorial comparison: for small k, primorial(k) < k!
    (since primes are sparse), but both grow super-exponentially.
    The ratio n!/P_n provides an e-related growth constant. -/
```

## Source Excerpt

```lean
def factorial_primorial_compare (k : TauIdx) : Nat × Nat :=
  (nat_factorial k, primorial k)
```
